import datetime
import inspect
import iris.exception as exception
import json
import logging
import os
import platform
import random
import re
import sys
import time
import yaml
from distutils.version import LooseVersion, StrictVersion

def configure_logger(loggerid=None, debug=False):
	if loggers.get(loggerid):
		return loggers.get(loggerid)
	else:
		level = logging.DEBUG if debug == True else logging.INFO

		logger = logging.getLogger(loggerid)
		handler = logging.StreamHandler()
		formatter = logging.Formatter("%(levelname)s %(message)s")
		handler.setFormatter(formatter)
		logger.addHandler(handler)
		logger.setLevel(level)
		logger.propagate = False
		loggers[loggerid] = logger
	return logger

def read_config(config_path=None):
	try:
		contents = open(config_path, "r").read()
		return contents
	except OSError as e:
		if e.errno == 2:
			raise exception.ConfigFileRead(path=config_path, message="No such file or directory")
		elif e.errno == 13:
			raise exception.ConfigFileRead(path=config_path, message="Permission denied")
		elif e.errno == 21:
			raise exception.ConfigFileRead(path=config_path, message="Is a directory")
		else:
			raise exception.ConfigFileRead(path=config_path, message=str(s))

def parse_config(profile=None):
	config_path = "{}/.iris.yml".format(os.path.expanduser("~"))
	contents = open(config_path, "r").read()

	if len(contents) <= 0:
		raise exception.InvalidConfigFile(path=config_path, message="Zero-length file")

	config = validate_yaml(contents)
	if config:
		if not "profiles" in config:
			raise exception.InvalidConfigFile(path=config_path, message="Missing profiles section")
	else:
		raise exception.InvalidConfigFile(path=config_path, message="File contains invalid YAML")

	if profile in config["profiles"]:
		if not "username" in config["profiles"][profile]:
			raise exception.InvalidProfile(profile=profile, message="No username specified in the profile")

		if not "password" in config["profiles"][profile]:
			raise exception.InvalidProfile(profile=profile, message="No placeId specified in the password")

		return config
	else:
		raise exception.MissingProfile(profile=profile)

def validate_yaml(string):
	if string:
		try:
			hash = yaml.load(string)
			return hash
		except:
			return None
	else:
		return None

def validate_json(string):
	if string:
		try:
			hash = json.loads(string)
			return hash
		except:
			return None
	else:
		return None

def date_to_timestamp(date=None):
	try:
		return int(time.mktime(datetime.datetime.strptime(date, "%Y-%m-%d").timetuple()))
	except:
		# create an exception
		raise(e)

def farenheit_to_celsius(temp):
	return (((temp - 32) * 5) / 9)

def celsius_to_farenheit(temp):
	return (((temp * 9) / 5) + 32)

def generate_random(length=8):
	return "".join(random.choice("0123456789abcdef") for x in range(length))

def make_response(client=None, success=None, content_key=None, content=None):
	client.success = success
	status = "success" if success == True else "error"

	if content_key:	
		return {"status": status, content_key: content}
	else:
		response = content
		response["status"] = status
		return response

def __missing_opts_error(method, missing):
	return "the following required {0} parameters are missing: {1}".format(method, ", ".join(missing))

def __disallowed_opts_error(method, disallowed):
	return "the following disallowed parameters were specified for the {0} method: {1}".format(method, ", ".join(disallowed))

def __missing_optional_error(method, oneof):
	return "the {0} method requires one of the following parameters: {1}".format(method, ", ".join(oneof))

def __too_many_optional_error(method, oneof):
	return "the {0} method will accept only one of the following parameters: {1}".format(method, ", ".join(oneof))

def process_parameters(opts=None, required=None, oneof=None, valid=None):
	content = {}
	errors = []
	method = inspect.stack()[1][3]
	ints = []
	booleans = []
	string_booleans = []
	dates = []

	if "params" not in valid:
		return content

	filtered = {k: v for k, v in opts.items() if v is not None}
	opts.clear()
	opts.update(filtered)

	missing = list( set(required) - set(opts.keys()) )
	if (len(missing) != 0):
		errors.append(__missing_opts_error(method, missing))

	# Find disallowed options
	#disallowed = list( set(opts.keys() - set(valid["params"])) )
	#if (len(disallowed) != 0):
	# errors.append(__disallowed_opts_error(method, disallowed))

	if len(oneof) > 0:
		for oneof_tuple in oneof:
			oneof_list = list(oneof_tuple)
			if len(set(oneof_list).intersection(opts.keys())) <= 0:
				errors.append(__missing_optional_error(method, oneof_list))

			if len(set(oneof_list).intersection(opts.keys())) > 1:
				errors.append(__too_many_optional_error(method, oneof_list))

	for param in valid["params"]:
		if param in opts and param in valid["params"]:

			if param in ints:
				if not isinstance(opts[param], int):
					try:
						opts[param] = int(opts[param])
					except:
						errors.append("{} must be an integer".format(param))

			if param in booleans:
				if isinstance(opts[param], bool):
					opts[param] = True if opts[param] == True else False
				elif isinstance(opts[param], str):
					opts[param] = True if opts[param].lower() == "true" else False
				else:
					opts[param] = "false"

			if param in string_booleans:
				if isinstance(opts[param], bool):
					opts[param] = "true" if opts[param] == True else "false"
				elif isinstance(opts[param], str):
					opts[param] = "true" if opts[param].lower() == "true" else "false"
				else:
					opts[param] = "false"

			if param in valid:
				if opts[param] in valid[param]:
					content[param] = opts[param]
				else:
					errors.append("{0} is an invalid {1}. valid options for the \"{2}\" parameter are: {3}".format(opts[param], param, param, ", ".join(valid[param])))
			else:
				content[param] = opts[param]

			if param in dates:
				if not re.match("^\d\d\d\d-\d\d-\d\d$", param):
					errors.append("{0} uses an invalid date format. The format for date fields should be YYYY-MM-DD.".format(param))

	if len(errors) > 0:
		for error in errors:
			logger.error(error)
		sys.exit(1)
	else:
		return content

# Begin python-specific
def __check_python_version(req_version):
	cur_version = sys.version_info
	if cur_version <= req_version:
		logger.fatal("Your Python interpreter is too old. Please upgrade to {}.{} or greater.".format(req_version[0], req_version[1]))
		sys.exit(1)

def check_environment():
	__check_python_version((3, 0))

def exception_name(e=None):
	try:
		return e.__class__.__name__
	except:
		return None

# End python-specific

version = sys.version_info
major = version[0]
loggers = {}
logger = configure_logger(loggerid="logger-{}".format(generate_random(length=32)), debug=False)


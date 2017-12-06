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


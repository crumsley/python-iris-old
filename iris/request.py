import inspect
import iris.utils as utils
import json
import os
import sys
from pprint import pprint

def send(client=None, payload=None, debug=False):
	method = __get_method(inspect.stack())
	payload = json.dumps(payload)
	client.response = {}
	client.logger.debug("Executing method: {0}".format(method))
	client.logger.debug("Sending payload: {}".format(payload))
	client.ws.send(payload)
	response = utils.validate_json(client.ws.recv())

	if "Error" in response["type"]:
		errors = []
		if "payload" in response and "attributes" in response["payload"]:
			attributes = response["payload"]["attributes"]
			if "errors" in attributes and isinstance(attributes["errors"], list):
				errors = ["code: {}, message: {}".format(e["attributes"]["code"], e["attributes"]["message"]) for e in attributes["errors"]]
			elif "code" in attributes and "message" in attributes:
				errors.append("code: {}, message: {}".format(attributes["code"], attributes["message"]))
		
		if len(errors) > 0:
			message = "; ".join(errors)
		else:
			message = "The method {} failed with an unknown error.".format(method)

		client.response = utils.make_response(client=client, success=False, content_key="message", content=message)

	else:
		client.response = utils.make_response(client=client, success=True, content=response)

def __get_method(stack):
	invalid_scripts = ["<module>", "__init__"]
	usable_bits = [frame for frame in stack if os.path.basename(frame[3]) not in invalid_scripts]
	return usable_bits[-1][3] if len(usable_bits) > 0 else "unknown method"
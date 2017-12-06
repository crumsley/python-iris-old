import inspect
import re
import sys
import websocket
import iris.authenticator as authenticator
import iris.exception as exception
import iris.payloads as payloads
import iris.request as request
import iris.utils as utils
import iris.devices
from pprint import pprint

class Iris(object):
	def __init__(self, **kwargs):
		global cookie
		global token

		self.success = None
		self.places = {}
		self.ws_uri = "wss://bc.irisbylowes.com/websocket"

		if not "profile" in kwargs:
			raise exception.MissingConstructorParameter(parameter="profile")

		self.debug = kwargs["debug"] if ("debug" in kwargs and isinstance(kwargs["debug"], bool)) else False
		self.logger = utils.configure_logger(debug=self.debug)

		auth = authenticator.Authenticator(
			profile=kwargs["profile"],
			debug=self.debug
		)
		auth.authenticate()
		token = auth.token
		cookie = "irisAuthToken={}".format(token)
		self.init()
		self.build_device_map()

	def init(self, **kwargs):
		self.ws = websocket.create_connection(
			self.ws_uri,
			cookie = cookie
		)
		# Get place ID from here
		result = utils.validate_json(self.ws.recv())
		self.get_place_id(result=result)

		# Set active place. REQUIRED.
		self.ws.send(payloads.set_active_place(place_id=self.place_id))
		result = utils.validate_json(self.ws.recv())

	def get_place_id(self, result):
		attributes = result["payload"]["attributes"]
		for place in attributes["places"]:
			name = place["placeName"]
			self.places[name] = place
		self.place_id = self.places[name]["placeId"]

	def build_device_map(self, **kwargs):
		self.response = {}; payload = {}
		self.list_devices()
		if self.success:
			self.devices = {}
			if "payload" in self.response["body"]:
				if "attributes" in self.response["body"]["payload"]:
					if "devices" in self.response["body"]["payload"]["attributes"]:
						if isinstance(self.response["body"]["payload"]["attributes"]["devices"], list):
							for device in self.response["body"]["payload"]["attributes"]["devices"]:
								device_name = device["dev:name"]
								self.devices[device_name] = device
			self.response = {}

		else:
			raise exception.DeviceMapError(message=self.response["body"])

	def close(self, **kwargs):
		self.ws.close()

	#def find_device(self, **kwargs):
	#	self.response = {}; payload = {}
	#	self.response = {
	#		"status": "success",
	#		"results": [obj for name, obj in self.devices.items() if obj["dev:devtypehint"] == "Thermostat"]
	#	}

	def battery_states(self, **kwargs):
		self.build_device_map()
		battery_states = []
		for name, obj in self.devices.items():
			if "devpow:source" in obj and obj["devpow:source"] == "BATTERY":
				battery_states.append({
					"name": obj["dev:name"],
					"vendor": obj["dev:vendor"],
					"model": obj["dev:model"],
					"battery": "{}%".format(obj["devpow:battery"]),
				})
		self.success = True
		self.response = {"status": "success", "results": battery_states}
		#if self.success:
		#	self.battery_states = []
		#	for name, obj in self.devices:


	def get_device(self, **kwargs):
		self.response = {}; payload = {}
		if kwargs["device"] in self.devices:
			device = self.devices[kwargs["device"]]
			self.success = True
			self.response["body"] = device
		else:
			self.success = False
			self.response = {"status": "error", "message": "device \"{}\" not found.".format(kwargs["device"])}

	def get_hub(self, **kwargs):
		request.send(
			client=self,
			payload=payloads.place(place_id=self.place_id, method="GetHub")
		)

	def hub_chime(self, **kwargs):
		request.send(
			client=self,
			payload=payloads.hub_chime(place_id=self.place_id)
		)

	def list_devices(self, **kwargs):
		request.send(
			client=self,
			payload=payloads.place(place_id=self.place_id, method="ListDevices")
		)
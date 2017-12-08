import inspect
import json
import os
import pkgutil
import re
import sys
import websocket
import iris.authenticator as authenticator
import iris.exception as exception
import iris.payloads as payloads
import iris.request as request
import iris.utils as utils
import iris.devices
import sys
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
		self.build_person_map()
		self.get_hub_id()

		#data = pkgutil.get_data("iris", "data/method-validator.json")
		#print(data)
		# This is a hack to get it to work until I can get python data to work
		pwd = os.path.dirname(os.path.realpath(__file__))
		vp = "{}/data/method-validator.json".format(pwd)
		self.validator = json.loads(open(vp, "r").read())

	def init(self, **kwargs):
		self.ws = websocket.create_connection(
			self.ws_uri,
			cookie = cookie
		)
		# Get place ID from here
		result = utils.validate_json(self.ws.recv())
		self.get_place_id(result=result)

		# Set active place. REQUIRED.
		payload = payloads.set_active_place(place_id=self.place_id)
		request.send(client=self, payload=payload, debug=self.debug)

	def get_hub_id(self, **kwargs):
		self.get_hub()
		if self.success:
			attributes = self.response["payload"]["attributes"]
			self.hub_id = attributes["hub"]["base:id"]
			self.hub_address = attributes["hub"]["base:address"]

	def get_place_id(self, result):
		attributes = result["payload"]["attributes"]
		for place in attributes["places"]:
			name = place["placeName"]
			self.places[name] = place
		self.place_id = self.places[name]["placeId"]
		self.account_id = self.places[name]["accountId"]

	def build_device_map(self, **kwargs):
		self.response = {}; payload = {}
		self.list_devices()
		
		if self.success:
			self.devices = self.response["payload"]["attributes"]["devices"]
		else:
			raise exception.DeviceMapError(message=self.response)

	def build_person_map(self, **kwargs):
		self.response = {}; payload = {}
		self.list_persons()
		if self.success:
			self.persons = self.response["payload"]["attributes"]["persons"]
			self.response = {}
		else:
			raise exception.PersonMapError(message=self.response)

	def close(self, **kwargs):
		self.ws.close()

	def get_hub(self, **kwargs):
		# sends <class 'iris.core.Iris'> as client
		request.send(
			client=self,
			payload=payloads.place(place_id=self.place_id, method="GetHub")
		)

	def list_devices(self, **kwargs):
		request.send(
			client=self,
			payload=payloads.place(place_id=self.place_id, method="ListDevices")
		)

	def list_persons(self, **kwargs):
		request.send(
			client=self,
			payload=payloads.place(place_id=self.place_id, method="ListPersons")
		)

	def get_address(self, type=None, id=None, name=None):
		addresses = []
		if type == "device":
			if id:
				addresses = [d["base:address"] for d in self.devices if d["base:id"] == id]
			elif name:
				addresses = [d["base:address"] for d in self.devices if d["dev:name"] == name]

		elif type == "person":
			if id:
				addresses = [p["base:address"] for p in self.persons if p["base:id"] == id]
			if name:
				addresses = [p["base:address"] for p in self.persons if "{} {}".format(p["person:firstName"], p["person:lastName"]).lower() == name.lower()]

		return addresses[0] if len(addresses) > 0 else None

	def get_id(self, type=None, name=None):
		ids = []
		if type == "device":
			ids = [d["base:id"] for d in self.devices if d["dev:name"] == name][0]

		elif type == "person":
			ids = [p["base:id"] for p in self.persons if "{} {}".format(p["person:firstName"], p["person:lastName"]).lower() == name.lower()][0]

		return ids[0] if len(ids) > 0 else None

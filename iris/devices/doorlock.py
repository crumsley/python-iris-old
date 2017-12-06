import iris.attributes as attributes
import iris.exception as exception
import iris.payloads as payloads
import iris.request as request
import iris.utils as utils
from pprint import pprint

class DoorLock(object):
	def __init__(self, **kwargs):
		self.success = None
		self.response = {}
		self.namespace = "doorlock"
		self.attributes = attributes[self.namespace]

		if "iris" in kwargs:
			self.iris = kwargs["iris"]
		else:
			raise exception.MissingConstructorParameter(parameter="iris")

		if not str(type(self.iris)) == "<class 'iris.core.Iris'>":
			raise exception.NotAnIrisCoreObject(class_name=str(type(self)))

		self.ws = self.iris.ws

	def door_lock(self, **kwargs):
		payload = payloads.set_attribute(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="lockstate",
			value="LOCKED",
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def door_unkocked(self, **kwargs):
		payload = payloads.set_attribute(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="lockstate",
			value="UNLOCKED",
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)
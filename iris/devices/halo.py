import iris.attributes as attributes
import iris.exception as exception
import iris.payloads as payloads
import iris.request as request
import iris.utils as utils
from pprint import pprint

class Halo(object):
	def __init__(self, **kwargs):
		self.success = None
		self.response = {}
		self.namespace = "halo"
		self.attributes = attributes[self.namespace]

		if "iris" in kwargs:
			self.iris = kwargs["iris"]
		else:
			raise exception.MissingConstructorParameter(parameter="iris")

		if not str(type(self.iris)) == "<class 'iris.core.Iris'>":
			raise exception.NotAnIrisCoreObject(class_name=str(type(self)))

		self.ws = self.iris.ws

	def set_room(self, **kwargs):
		setpoint = kwargs["room"]
		payload = payloads.set_attribute(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="room",
			value=room,
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def set_haloalertstate(self, **kwargs):
		setpoint = kwargs["state"]
		payload = payloads.set_attribute(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="haloalertstate",
			value=state,
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)
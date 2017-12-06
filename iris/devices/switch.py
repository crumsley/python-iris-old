import iris.attributes as attributes
import iris.exception as exception
import iris.payloads as payloads
import iris.request as request
import iris.utils as utils
from pprint import pprint

class Switch(object):
	def __init__(self, **kwargs):
		self.success = None
		self.response = {}
		self.namespace = "swit"
		self.attributes = attributes.devices[self.namespace]

		if "iris" in kwargs:
			self.iris = kwargs["iris"]
		else:
			raise exception.MissingConstructorParameter(parameter="iris")

		if not str(type(self.iris)) == "<class 'iris.core.Iris'>":
			raise exception.NotAnIrisCoreObject(class_name=str(type(self)))

		self.ws = self.iris.ws

	def switch_on(self, **kwargs):
		payload = payloads.set_attribute(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="state",
			value="ON",
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def switch_off(self, **kwargs):
		payload = payloads.set_attribute(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="state",
			value="OFF",
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

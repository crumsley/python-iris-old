import iris.attributes as attributes
import iris.exception as exception
import iris.payloads as payloads
import iris.request as request
import iris.utils as utils
import sys
from pprint import pprint

class Thermostat(object):
	def __init__(self, **kwargs):
		self.success = None
		self.response = {}
		self.namespace = "therm"
		self.attributes = attributes.devices[self.namespace]

		if "iris" in kwargs:
			self.iris = kwargs["iris"]
		else:
			raise exception.MissingConstructorParameter(parameter="iris")

		if not str(type(self.iris)) == "<class 'iris.core.Iris'>":
			raise exception.NotAnIrisCoreObject(class_name=str(type(self)))

		self.ws = self.iris.ws

	def set_coolsetpoint(self, **kwargs):
		setpoint = kwargs["setpoint"]
		payload = payloads.set_attribute(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="coolsetpoint",
			value=utils.farenheit_to_celsius(setpoint),
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def set_heatsetpoint(self, **kwargs):
		setpoint = kwargs["setpoint"]
		payload = payloads.set_attribute(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="heatsetpoint",
			value=utils.farenheit_to_celsius(setpoint),
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def set_hvacmode(self, **kwargs):
		mode = kwargs["mode"]
		payload = payloads.set_attribute(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="hvacmode",
			value=mode
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def set_fanmode(self, **kwargs):
		mode = kwargs["mode"]
		payload = payloads.set_attribute(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="fanmode",
			value=mode
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def set_emergencyheat(self, **kwargs):
		mode = kwargs["mode"]
		payload = payloads.set_attribute(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="emergencyheat",
			value=mode
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def set_controlmode(self, **kwargs):
		mode = kwargs["mode"]
		payload = payloads.set_attribute(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="controlmode",
			value=mode
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def set_filterlifespanruntime(self, **kwargs):
		hours = kwargs["hours"]
		payload = payloads.set_attribute(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="filterlifespanruntime",
			value=hours
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def set_filterlifespandays(self, **kwargs):
		days = kwargs["days"]
		payload = payloads.set_attribute(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="filterlifespandays",
			value=days
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)


import iris.payloads as payloads
import iris.request as request
import iris.utils as utils
import sys
from iris.devices.device import Device
from pprint import pprint

class Thermostat(object):
	def __init__(self, **kwargs):
		Device.__init__(self, **kwargs)
		self.namespace = "therm"

	def __therm_request(self, **kwargs):
			type = None
			value = None
			method = kwargs["method"]
			self.response = {}; payload = {}
			required, oneof, valid = utils.fetch_parameters(self.namespace, method, self.iris.validator)
			content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
			if isinstance(content, dict):
				if "device_name" in content:
					type = "name"
					value = content["device_name"]
					device_address = self.iris.get_address(type="device", name=content["device_name"])
				elif "device_id" in content:
					type = "ID"
					value = content["device_id"]
					device_address = self.iris.get_address(type="device", id=content["device_id"])

				if device_address:
					payload = payloads.therm_method(
						namespace=self.namespace,
						device_address=device_address,
						method=method,
					)
					for k, v in content.items(): payload["payload"]["attributes"][k] = v
					request.send(client=self, payload=payload, debug=self.iris.debug)
				else:
					self.response = utils.make_response(client=self, success=False, content="The device with the {} {} does not exist.".format(type, value))


	def change_filter(self, **kwargs):
		kwargs["method"] = "changeFilter"
		self.__therm_request(**kwargs)

	def set_coolsetpoint(self, **kwargs):
		setpoint = kwargs["setpoint"]
		payload = payloads.set_attributes(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="coolsetpoint",
			value=utils.farenheit_to_celsius(setpoint),
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def set_heatsetpoint(self, **kwargs):
		setpoint = kwargs["setpoint"]
		payload = payloads.set_attributes(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="heatsetpoint",
			value=utils.farenheit_to_celsius(setpoint),
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def set_hvacmode(self, **kwargs):
		mode = kwargs["mode"]
		payload = payloads.set_attributes(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="hvacmode",
			value=mode
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def set_fanmode(self, **kwargs):
		mode = kwargs["mode"]
		payload = payloads.set_attributes(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="fanmode",
			value=mode
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def set_emergencyheat(self, **kwargs):
		mode = kwargs["mode"]
		payload = payloads.set_attributes(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="emergencyheat",
			value=mode
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def set_controlmode(self, **kwargs):
		mode = kwargs["mode"]
		payload = payloads.set_attributes(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="controlmode",
			value=mode
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def set_filterlifespanruntime(self, **kwargs):
		hours = kwargs["hours"]
		payload = payloads.set_attributes(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="filterlifespanruntime",
			value=hours
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def set_filterlifespandays(self, **kwargs):
		days = kwargs["days"]
		payload = payloads.set_attributes(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="filterlifespandays",
			value=days
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

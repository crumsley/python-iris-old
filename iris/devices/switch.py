import iris.payloads as payloads
import iris.request as request
from iris.devices.device import Device

class Switch(Device):
	def __init__(self, **kwargs):
		Device.__init__(self, **kwargs)

		self.namespace = "swit"

	def switch_on(self, **kwargs):
		payload = payloads.set_attributes(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="state",
			value="ON",
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def switch_off(self, **kwargs):
		payload = payloads.set_attributes(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="state",
			value="OFF",
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

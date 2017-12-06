import iris.attributes as attributes
import iris.payloads as payloads
import iris.request as request
from iris.devices.device import Device

class Dimmer(Device):
	def __init__(self, **kwargs):
		Device.__init__(self, **kwargs)

		self.namespace = "dimmer"
		self.attributes = attributes[self.namespace]

	def set_brightness(self, **kwargs):
		level = kwargs["level"]
		payload = payloads.set_attributes(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="brightness",
			value=level,
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

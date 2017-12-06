import iris.attributes as attributes
import iris.payloads as payloads
from iris.devices.device import Device

class Light(object):
	def __init__(self, **kwargs):
		Device.__init__(self, **kwargs)

		self.namespace = "light"
		self.attributes = attributes.devices[self.namespace]

	def colormode(self, **kwargs):
		mode = kwargs["mode"]
		payload = payloads.set_attribute(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="colormode",
			value=mode,
		)
		request.send(client=self, payload=payload)

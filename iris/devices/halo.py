import iris.attributes as attributes
import iris.payloads as payloads
import iris.request as request
from iris.devices.device import Device

class Halo(object):
	def __init__(self, **kwargs):
		Device.__init__(self, **kwargs)

		self.namespace = "halo"
		self.attributes = attributes.devices[self.namespace]

	def set_room(self, **kwargs):
		setpoint = kwargs["room"]
		payload = payloads.set_attributes(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="room",
			value=room,
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def set_haloalertstate(self, **kwargs):
		setpoint = kwargs["state"]
		payload = payloads.set_attributes(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="haloalertstate",
			value=state,
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)
import iris.payloads as payloads
import iris.request as request
from iris.devices.device import Device

class DoorLock(object):
	def __init__(self, **kwargs):
		Device.__init__(self, **kwargs)

		self.namespace = "doorlock"

	def door_lock(self, **kwargs):
		payload = payloads.set_attributes(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="lockstate",
			value="LOCKED",
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def door_unkocked(self, **kwargs):
		payload = payloads.set_attributes(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="lockstate",
			value="UNLOCKED",
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)
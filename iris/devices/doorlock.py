import iris.payloads as payloads
import iris.request as request
from iris.devices.device import Device

class DoorLock(object):
	def __init__(self, **kwargs):
		Device.__init__(self, **kwargs)

		self.namespace = "doorlock"

	def __doorlock_request(self, **kwargs):
		namespace = self.namespace
		method = kwargs["method"]
		self.response = {}; payload = {}
		required, valid = utils.fetch_parameters(namespace, method, self.iris.validator)
		content = utils.process_parameters(opts=kwargs, required=required, valid=valid)
		if isinstance(content, dict):
			payload = payloads.doorlock_method(
				namespace=namespace,
				account_id=self.iris.account_id,
				method=method,
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def authorize_person(self, **kwargs):
		kwargs["method"] = "AuthorizePerson"
		self.__doorlock_request(**kwargs)

	def deauthorize_person(self, **kwargs):
		kwargs["method"] = "DeauthorizePerson"
		self.__doorlock_request(**kwargs)

	def buzz_in(self, **kwargs):
		kwargs["method"] = "BuzzIn"
		self.__doorlock_request(**kwargs)

	def clear_all_pins(self, **kwargs):
		kwargs["method"] = "ClearAllPins"
		self.__doorlock_request(**kwargs)

	def lock_door(self, **kwargs):
		payload = payloads.set_attributes(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="lockstate",
			value="LOCKED",
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def unlock_door(self, **kwargs):
		payload = payloads.set_attributes(
			place_id=self.iris.place_id,
			device_id=self.iris.devices[kwargs["device"]]["base:id"],
			namespace=self.namespace,
			key="lockstate",
			value="UNLOCKED",
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)
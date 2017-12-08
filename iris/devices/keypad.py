import iris.payloads as payloads
import iris.request as request
import iris.utils as utils
from iris.devices.device import Device

class Keypad(Device):
	def __init__(self, **kwargs):
		Device.__init__(self, **kwargs)

		self.namespace = "keypad"

	def __keypad_request(self, **kwargs):
		namespace = self.namespace
		method = kwargs["method"]
		self.response = {}; payload = {}
		required, valid = utils.fetch_parameters(namespace, method, self.iris.validator)
		content = utils.process_parameters(opts=kwargs, required=required, valid=valid)
		if isinstance(content, dict):
			payload = payloads.keypad_method(
				namespace=namespace,
				account_id=self.iris.account_id,
				method=method,
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def begin_arming(self, **kwargs):
		kwargs["method"] = "BeginArming"
		self.__keypad_request(**kwargs)

	def armed(self, **kwargs):
		kwargs["method"] = "Armed"
		self.__keypad_request(**kwargs)

	def disarmed(self, **kwargs):
		kwargs["method"] = "Disarmed"
		self.__keypad_request(**kwargs)

	def soaking(self, **kwargs):
		kwargs["method"] = "soaking"
		self.__keypad_request(**kwargs)

	def alerting(self, **kwargs):
		kwargs["method"] = "alerting"
		self.__keypad_request(**kwargs)

	def chime(self, **kwargs):
		kwargs["method"] = "chime"
		self.__keypad_request(**kwargs)
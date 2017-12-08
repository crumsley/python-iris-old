import iris.payloads as payloads
import iris.request as request
import iris.utils as utils
from iris.devices.device import Device

class Account(Device):
	def __init__(self, **kwargs):
		Device.__init__(self, **kwargs)

		self.namespace = "account"

	def __account_request(self, **kwargs):
		#namespace = kwargs["namespace"]
		namespace = self.namespace
		method = kwargs["method"]
		self.response = {}; payload = {}
		required, valid = utils.fetch_parameters(namespace, method, self.iris.validator)
		content = utils.process_parameters(opts=kwargs, required=required, valid=valid)
		if isinstance(content, dict):
			payload = payloads.account_method(
				namespace=namespace,
				account_id=self.iris.account_id,
				method=method,
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def list_adjustments(self, **kwargs):
		kwargs["method"] = "ListAdjustments"
		self.__account_request(**kwargs)

	def list_devices(self, **kwargs):
		kwargs["method"] = "ListDevices"
		self.__account_request(**kwargs)

	def list_hubs(self, **kwargs):
		kwargs["method"] = "ListHubs"
		self.__account_request(**kwargs)		

	def list_invoices(self, **kwargs):
		kwargs["method"] = "ListInvoices"
		self.__account_request(**kwargs)

	def list_places(self, **kwargs):
		kwargs["method"] = "ListPlaces"
		self.__account_request(**kwargs)
	def __account(self, **kwargs):
		payload = payloads.account(
			account_id=self.iris.account_id,
			method=kwargs["method"]
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

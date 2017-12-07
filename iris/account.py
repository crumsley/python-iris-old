import iris.attributes as attributes
import iris.payloads as payloads
import iris.request as request
from iris.devices.device import Device

class Account(Device):
	def __init__(self, **kwargs):
		Device.__init__(self, **kwargs)

		self.namespace = "account"
		#self.attributes = attributes[self.namespace]

	def list_adjustments(self, **kwargs):
		self.__account(method="ListAdjustments")

	def list_devices(self, **kwargs):
		self.__account(method="ListDevices")

	def list_devices(self, **kwargs):
		self.__account(method="ListDevices")

	def list_hubs(self, **kwargs):
		self.__account(method="ListHubs")

	def list_invoices(self, **kwargs):
		self.__account(method="ListInvoices")

	def list_places(self, **kwargs):
		self.__account(method="ListPlaces")

	def __account(self, **kwargs):
		payload = payloads.account(
			account_id=self.iris.account_id,
			method=kwargs["method"]
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

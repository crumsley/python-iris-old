import iris.attributes as attributes
import iris.payloads as payloads
import iris.request as request
from iris.devices.device import Device

class Person(Device):
	def __init__(self, **kwargs):
		Device.__init__(self, **kwargs)

		self.namespace = "person"
		#self.attributes = attributes[self.namespace]
		print(type(self.iris))

	def list_persons(self, **kwargs):
		payload = payloads.place(
			place_id=self.iris.place_id,
			method="ListPersons"
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def list_history_entries(self, **kwargs):
		address = self.iris.get_base_address(type="person", name=kwargs["name"])
		if address:
			payload = payloads.person(
				namespace=self.namespace,
				address=address,
				method="ListHistoryEntries"
			)
			request.send(client=self, payload=payload, debug=self.iris.debug)
		else:
			self.response = self.iris.make_response(
				success=False,
				content_key="message",
				content="User {} not found.".format(kwargs["name"])
			)

	def get_security_answers(self, **kwargs):
		address = self.iris.get_base_address(type="person", name=kwargs["name"])
		if address:
			payload = payloads.person(
				namespace=self.namespace,
				address=address,
				method="GetSecurityAnswers"
			)
			request.send(client=self, payload=payload, debug=self.iris.debug)
		else:
			self.response = self.iris.make_response(
				success=False,
				content_key="message",
				content="User {} not found.".format(kwargs["name"])
			)
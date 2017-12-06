import iris.attributes as attributes
import iris.payloads as payloads
import iris.request as request
from iris.devices.device import Device

class Person(Device):
	def __init__(self, **kwargs):
		Device.__init__(self, **kwargs)

		self.namespace = "person"
		#self.attributes = attributes[self.namespace]

	def list_persons(self, **kwargs):
		payload = payloads.place(
			place_id=self.iris.place_id,
			method="ListPersons"
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def list_history_entries(self, **kwargs):
		name = kwargs["name"]
		payload = payloads.person(
			namespace=self.namespace,
			address=self.iris.persons[name]["base:address"],
			method="ListHistoryEntries"
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def get_security_answers(self, **kwargs):
		name = kwargs["name"]
		payload = payloads.person(
			namespace=self.namespace,
			address=self.iris.persons[name]["base:address"],
			method="GetSecurityAnswers"
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)
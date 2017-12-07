import iris.payloads as payloads
import iris.request as request
import iris.utils as utils
from iris.devices.device import Device

class Person(Device):
	def __init__(self, **kwargs):
		Device.__init__(self, **kwargs)

		self.namespace = "person"

	def list_persons(self, **kwargs):
		payload = payloads.place(
			place_id=self.iris.place_id,
			method="ListPersons"
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def list_history_entries(self, **kwargs):
		person_id = self.iris.get_id(type="person", name=kwargs["name"])
		if person_id:
			payload = payloads.person(
				namespace=self.namespace,
				person_id=person_id,
				method="ListHistoryEntries"
			)
			request.send(client=self, payload=payload, debug=self.iris.debug)
		else:
			self.response = utils.make_response(
				client=self,
				success=False,
				content_key="message",
				content="User {} not found.".format(kwargs["name"])
			)

	def list_mobile_devices(self, **kwargs):
		person_id = self.iris.get_id(type="person", name=kwargs["name"])
		if person_id:
			payload = payloads.person(
				namespace=self.namespace,
				person_id=person_id,
				method="ListMobileDevices"
			)
			request.send(client=self, payload=payload, debug=self.iris.debug)
		else:
			self.response = utils.make_response(
				client=self,
				success=False,
				content_key="message",
				content="User {} not found.".format(kwargs["name"])
			)

	def get_security_answers(self, **kwargs):
		person_id = self.iris.get_id(type="person", name=kwargs["name"])
		if person_id:
			payload = payloads.person(
				namespace=self.namespace,
				person_id=person_id,
				method="GetSecurityAnswers"
			)
			request.send(client=self, payload=payload, debug=self.iris.debug)
		else:
			self.response = utils.make_response(
				client=self,
				success=False,
				content_key="message",
				content="User {} not found.".format(kwargs["name"])
			)
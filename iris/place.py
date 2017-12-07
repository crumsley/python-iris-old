import iris.payloads as payloads
import iris.request as request
import iris.utils as utils
from iris.devices.device import Device

class Place(Device):
	def __init__(self, **kwargs):
		Device.__init__(self, **kwargs)

		self.namespace = "place"

	def list_persons(self, **kwargs):
		payload = payloads.place(
			place_id=self.iris.place_id,
			method="ListPersons"
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def create_invitation(self, **kwargs):
		self.response = {}; payload = {}
		required = ["firstName", "lastName", "email"]
		oneof = []
		valid = {
			"params": ["firstName", "lastName", "email", "relationship"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.place(
				place_id=self.iris.place_id,
				method="CreateInvitation",
			)
			payload["payload"]["attributes"]["firstName"] = content["firstName"]
			payload["payload"]["attributes"]["lastName"] = content["lastName"]
			payload["payload"]["attributes"]["email"] = content["email"]
			if "relationship" in content: payload["payload"]["attributes"]["relationship"] = content["relationship"]
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def list_hubs(self, **kwargs):
		self.response = {}; payload = {}
		required = []
		oneof = []
		valid = {}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.place(
				place_id=self.iris.place_id,
				method="ListHubs",
			)
			request.send(client=self, payload=payload, debug=self.iris.debug)
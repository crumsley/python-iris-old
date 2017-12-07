import iris.attributes as attributes
import iris.payloads as payloads
import iris.request as request
from iris.devices.device import Device

class Hub(Device):
	def __init__(self, **kwargs):
		Device.__init__(self, **kwargs)

		self.namespace = "hub"
		#self.attributes = attributes[self.namespace]

	## account ##
	def list_hubs(self, **kwargs):
		payload = payloads.account(
			account_id=self.iris.account_id,
			method="ListHubs"
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	## hub ##
	def chime(self, **kwargs):
		payload = payloads.hub(
			hub_address=self.iris.hub_address,
			method="chime"
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)		

	def get_logs(self, **kwargs):
		payload = payloads.hub(
			hub_address=self.iris.hub_address,
			method="GetLogs"
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def pairing_request(self, **kwargs):
		# actionType: "START_PAIRING,STOP_PAIRING"
		# timeout: "The amount of time in milliseconds for which the place will be able to add devices"
		payload = payloads.hub(
			hub_address=self.iris.hub_address,
			method="PairingRequest"
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def reset_log_level(self, **kwargs):
		payload = payloads.hub(
			hub_address=self.iris.hub_address,
			method="ResetLogLevel"
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def set_log_level(self, **kwargs):
		# level: "TRACE,DEBUG,INFO,WARN,ERROR"
		# scope: "ROOT,AGENT,ZIGBEE,ZWAVE,BLE,SERCOMM" optional
		payload = payloads.hub(
			hub_address=self.iris.hub_address,
			method="SetLogLevel"
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def unpairing_request(self, **kwargs):
		# actionType: "START_UNPAIRING,STOP_UNPAIRING"
		# protocol: "The namespace of the protocol of the device expected to be removed. By default no device is expected to be removed."
		# protocolId: "The protocolId of the device expected to be removed. By default no device is expected to be removed."
		# force: boolean
		payload = payloads.hub(
			hub_address=self.iris.hub_address,
			method="UnpairingRequest"
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def get_config(self, **kwargs):
		payload = payloads.hub(
			hub_address=self.iris.hub_address,
			method="GetConfig"
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	## hubadvanced ##
	def factory_reset(self, **kwargs):
		payload = payloads.hubadv(
			hub_address=self.iris.hub_address,
			method="FactoryReset"
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def get_device_info(self, **kwargs):
		payload = payloads.hubadv(
			hub_address=self.iris.hub_address,
			method="GetDeviceInfo"
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def get_known_devices(self, **kwargs):
		payload = payloads.hubadv(
			hub_address=self.iris.hub_address,
			method="GetKnownDevices"
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def reboot(self, **kwargs):
		payload = payloads.hubadv(
			hub_address=self.iris.hub_address,
			method="Reboot"
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def restart(self, **kwargs):
		payload = payloads.hubadv(
			hub_address=self.iris.hub_address,
			method="Restart"
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	## hubbackup ##
	def backup(self, **kwargs):
		payload = payloads.hubbackup(
			hub_address=self.iris.hub_address,
			method="Backup"
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def restore(self, **kwargs):
		payload = payloads.hubbackup(
			hub_address=self.iris.hub_address,
			method="Restore"
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	## hubdebug ##
	def get_bootlog(self, **kwargs):
		payload = payloads.hubdebug(
			hub_address=self.iris.hub_address,
			method="GetBootLog"
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def get_processes(self, **kwargs):
		payload = payloads.hubdebug(
			hub_address=self.iris.hub_address,
			method="GetProcesses"
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

	def get_syslog(self, **kwargs):
		payload = payloads.hubdebug(
			hub_address=self.iris.hub_address,
			method="GetSyslog"
		)
		request.send(client=self, payload=payload, debug=self.iris.debug)

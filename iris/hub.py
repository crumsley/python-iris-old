import iris.payloads as payloads
import iris.request as request
import iris.utils as utils
from iris.devices.device import Device

class Hub(Device):
	def __init__(self, **kwargs):
		Device.__init__(self, **kwargs)

		self.namespace = "hub"

	## hub ##
	def get_config(self, **kwargs):
		self.response = {}; payload = {}
		required = []
		oneof = []
		valid = {
			"params": ["defaults", "matching"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hub(
				hub_address=self.iris.hub_address,
				method="GetConfig",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def get_logs(self, **kwargs):
		self.response = {}; payload = {}
		required = []
		oneof = []
		valid = {}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hub(
				hub_address=self.iris.hub_address,
				method="GetLogs",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def pairing_request(self, **kwargs):
		self.response = {}; payload = {}
		required = ["actionType", "timeout"]
		oneof = []
		valid = {
			"params": ["actionType", "timeout"],
			"actionType": ["START_PAIRING", "STOP_PAIRING"],
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hub(
				hub_address=self.iris.hub_address,
				method="PairingRequest",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def reset_log_level(self, **kwargs):
		self.response = {}; payload = {}
		required = []
		oneof = []
		valid = {}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hub(
				hub_address=self.iris.hub_address,
				method="ResetLogLevel",
			)
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def set_log_level(self, **kwargs):
		self.response = {}; payload = {}
		required = ["level"]
		oneof = []
		valid = {
			"params": ["level", "scope"],
			"level": ["TRACE", "DEBUG", "INFO", "WARN", "ERROR"],
			"scope": ["ROOT", "AGENT", "ZIGBEE", "ZWAVE", "BLE", "SERCOMM"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hub(
				hub_address=self.iris.hub_address,
				method="ResetLogLevel",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def steam_logs(self, **kwargs):
		self.response = {}; payload = {}
		required = ["duration"]
		oneof = []
		valid = {
			"params": ["duration", "severity"],
			"severity": ["TRACE", "DEBUG", "INFO", "WARN", "ERROR"],
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hub(
				hub_address=self.iris.hub_address,
				method="StreamLogs",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def unpairing_request(self, **kwargs):
		self.response = {}; payload = {}
		required = ["actionType", "timeout"]
		oneof = []
		valid = {
			"params": ["actionType", "timeout", "protocol", "protocolId", "force"],
			"actionType": ["START_UNPAIRING", "STOP_UNPAIRING"],
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hub(
				hub_address=self.iris.hub_address,
				method="UnpairingRequest",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	## hub4g ##
	def lte_get_info(self, **kwargs):
		self.response = {}; payload = {}
		required = []
		oneof = []
		valid = {}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hub4g(
				hub_address=self.iris.hub_address,
				method="GetInfo",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def lte_get_statistics(self, **kwargs):
		self.response = {}; payload = {}
		required = []
		oneof = []
		valid = {}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hub4g(
				hub_address=self.iris.hub_address,
				method="GetStatistics",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def lte_reset_statistics(self, **kwargs):
		self.response = {}; payload = {}
		required = []
		oneof = []
		valid = {}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hub4g(
				hub_address=self.iris.hub_address,
				method="ResetStatistics",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	## hubadv ##
	def factory_reset(self, **kwargs):
		self.response = {}; payload = {}
		required = []
		oneof = []
		valid = {}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubadv(
				hub_address=self.iris.hub_address,
				method="FactoryReset",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def firmware_update(self, **kwargs):
		self.response = {}; payload = {}
		required = ["url"]
		oneof = []
		valid = {
			"params": ["url", "priority", "type"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubadv(
				hub_address=self.iris.hub_address,
				method="FirmwareUpdate",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def get_device_info(self, **kwargs):
		self.response = {}; payload = {}
		required = ["protocolAddress"]
		oneof = []
		valid = {
			"params": ["protocolAddress"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubadv(
				hub_address=self.iris.hub_address,
				method="GetDeviceInfo",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def get_known_devices(self, **kwargs):
		self.response = {}; payload = {}
		required = ["protocols"]
		oneof = []
		valid = {
			"params": ["protocols"] # lists???
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubadv(
				hub_address=self.iris.hub_address,
				method="GetKnownDevices",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def reboot(self, **kwargs):
		self.response = {}; payload = {}
		required = []
		oneof = []
		valid = {}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubadv(
				hub_address=self.iris.hub_address,
				method="Reboot",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def restart(self, **kwargs):
		self.response = {}; payload = {}
		required = []
		oneof = []
		valid = {}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubadv(
				hub_address=self.iris.hub_address,
				method="Restart",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	## hubalarm ##
	def alarm_activate(self, **kwargs):
		self.response = {}; payload = {}
		required = []
		oneof = []
		valid = {}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubalarm(
				hub_address=self.iris.hub_address,
				method="Activate",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def alarm_arm(self, **kwargs):
		self.response = {}; payload = {}
		required = []
		oneof = []
		valid = {
			"params": ["mode", "bypassed", "entranceDelaySecs", "exitDelaySecs", "alarmSensitivityDeviceCount", "silent",
				"soundsEnabled", "activeDevices", "armedBy", "armedFrom"],
			"mode": ["ON", "PARTIAL"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubalarm(
				hub_address=self.iris.hub_address,
				method="Arm",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def alarm_clear_incident(self, **kwargs):
		self.response = {}; payload = {}
		required = []
		oneof = []
		valid = {}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubalarm(
				hub_address=self.iris.hub_address,
				method="ClearIncident",
			)
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def alarm_disarm(self, **kwargs):
		self.response = {}; payload = {}
		required = []
		oneof = []
		valid = {
			"params": ["disarmedBy", "disarmedFrom"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubalarm(
				hub_address=self.iris.hub_address,
				method="Disarm",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def alarm_panic(self, **kwargs):
		self.response = {}; payload = {}
		required = []
		oneof = []
		valid = {
			"params": ["source", "event"],
			"event": ["RULE", "VERIFIED_ALARM"],
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubalarm(
				hub_address=self.iris.hub_address,
				method="Panic",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def alarm_suspend(self, **kwargs):
		self.response = {}; payload = {}
		required = []
		oneof = []
		valid = {}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubalarm(
				hub_address=self.iris.hub_address,
				method="Suspend",
			)
			request.send(client=self, payload=payload, debug=self.iris.debug)

	## hubbackup ##
	def backup(self, **kwargs):
		self.response = {}; payload = {}
		required = ["type"]
		oneof = []
		valid = {
			"params": ["type", "output_file"],
			"type": ["V2"],
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubbackup(
				hub_address=self.iris.hub_address,
				method="Backup",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def restore(self, **kwargs):
		self.response = {}; payload = {}
		required = ["type", "data"]
		oneof = []
		valid = {
			"params": ["type"],
			"type": ["V1", "V2"],
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubbackup(
				hub_address=self.iris.hub_address,
				method="Restore",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	## hubchime ##
	def chime(self, **kwargs):
		self.response = {}; payload = {}
		required = []
		oneof = []
		valid = {}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubbackup(
				hub_address=self.iris.hub_address,
				method="Chime",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	## hubdebug ##
	def exec_process(self, **kwargs):
		self.response = {}; payload = {}
		required = ["cmd"]
		oneof = []
		valid = {
			"params": ["cmd", "args", "stdin", "timeout"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubdebug(
				hub_address=self.iris.hub_address,
				method="ExecProcess",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def get_agent_db(self, **kwargs):
		self.response = {}; payload = {}
		required = []
		oneof = []
		valid = {}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubdebug(
				hub_address=self.iris.hub_address,
				method="GetAgentDb",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def get_bootlog(self, **kwargs):
		self.response = {}; payload = {}
		required = []
		oneof = []
		valid = {}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubdebug(
				hub_address=self.iris.hub_address,
				method="GetBootlog",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def get_load(self, **kwargs):
		self.response = {}; payload = {}
		required = []
		oneof = []
		valid = {}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubdebug(
				hub_address=self.iris.hub_address,
				method="GetLoad",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def get_processes(self, **kwargs):
		self.response = {}; payload = {}
		required = []
		oneof = []
		valid = {}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubdebug(
				hub_address=self.iris.hub_address,
				method="GetProcesses",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def get_syslog(self, **kwargs):
		self.response = {}; payload = {}
		required = []
		oneof = []
		valid = {}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubdebug(
				hub_address=self.iris.hub_address,
				method="GetSyslog",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	## hubmetrics ##
	def end_metrics_job(self, **kwargs):
		self.response = {}; payload = {}
		required = ["jobname"]
		oneof = []
		valid = {
			"params": ["jobname"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubmetrics(
				hub_address=self.iris.hub_address,
				method="EndMetricsJob",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def get_metrics_job_info(self, **kwargs):
		self.response = {}; payload = {}
		required = ["jobname"]
		oneof = []
		valid = {
			"params": ["jobname"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubmetrics(
				hub_address=self.iris.hub_address,
				method="GetMetricsJobInfo",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def get_stored_metrics(self, **kwargs):
		self.response = {}; payload = {}
		required = []
		oneof = []
		valid = {}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubmetrics(
				hub_address=self.iris.hub_address,
				method="GetStoredMetrics",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def list_metrics(self, **kwargs):
		self.response = {}; payload = {}
		required = ["regex"]
		oneof = []
		valid = {
			"params": ["regex"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubmetrics(
				hub_address=self.iris.hub_address,
				method="GetMetricsJobInfo",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def start_metrics_job(self, **kwargs):
		self.response = {}; payload = {}
		required = ["jobname", "periodMs", "durationMs", "metrics"]
		oneof = []
		valid = {
			"params": ["jobname", "periodMs", "durationMs", "metrics"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubmetrics(
				hub_address=self.iris.hub_address,
				method="StartMetricsJob",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	## hubnetwork ##
	def get_routing_table(self, **kwargs):
		# Message type [hubnet:GetRoutingTable] is not supported
		self.response = {}; payload = {}
		required = []
		oneof = []
		valid = {}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubnet(
				hub_address=self.iris.hub_address,
				method="GetRoutingTable",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	## hubsercomm ##
	def get_camera_password(self, **kwargs):
		self.response = {}; payload = {}
		required = []
		oneof = []
		valid = {}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="getCameraPassword",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def pair_camera(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac"]
		oneof = []
		valid = {
			"params": ["mac"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="pair",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def factory_reset_camera(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac"]
		oneof = []
		valid = {
			"params": ["mac"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="reset",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def reboot_camera(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac"]
		oneof = []
		valid = {
			"params": ["mac"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="reboot",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def configure_camera(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac", "params"]
		oneof = []
		valid = {
			"params": ["mac", "params"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="config",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def upgrade_camera_firmware(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac", "url"]
		oneof = []
		valid = {
			"params": ["mac", "url"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="config",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def get_camera_state(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac"]
		oneof = []
		valid = {
			"params": ["mac"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="getState",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def get_camera_version(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac"]
		oneof = []
		valid = {
			"params": ["mac"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="getVersion",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def get_camera_day_night_setting(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac"]
		oneof = []
		valid = {
			"params": ["mac"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="getDayNight",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def get_camera_ipv4(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac"]
		oneof = []
		valid = {
			"params": ["mac"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="getIPAddress",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def get_camera_model(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac"]
		oneof = []
		valid = {
			"params": ["mac"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="getModel",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def get_camera_info(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac"]
		oneof = []
		valid = {
			"params": ["mac"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="getInfo",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def get_camera_attributes(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac"]
		oneof = []
		valid = {
			"params": ["mac"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="getAttrs",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def start_camera_motion_detection(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac", "url"]
		oneof = []
		valid = {
			"params": ["mac", "url", "username", "password"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="motionDetectStart",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def stop_camera_motion_detection(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac"]
		oneof = []
		valid = {
			"params": ["mac"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="motionDetectStop",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def start_camera_video_stream(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac", "address", "username", "password"]
		oneof = []
		valid = {
			"params": ["mac", "address", "username", "password", "duration", "precapture", "format",
				"resolution", "quality_type", "bitrate", "quality", "framerate", "status"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="videoStreamStart",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def stop_camera_video_stream(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac"]
		oneof = []
		valid = {
			"params": ["mac"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="videoStreamStop",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def start_camera_wifi_scan(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac"]
		oneof = []
		valid = {
			"params": ["mac"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="wifiScanStart",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def end_camera_wifi_scan(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac"]
		oneof = []
		valid = {
			"params": ["mac"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="wifiScanEnd",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def camera_wifi_connect(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac", "ssid", "security"]
		oneof = []
		valid = {
			"params": ["mac", "ssid", "security", "key"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="wifiConnect",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def camera_wifi_disconnect(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac"]
		oneof = []
		valid = {
			"params": ["mac"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="wifiConnect",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def camera_get_wifi_attributes(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac"]
		oneof = []
		valid = {
			"params": ["mac"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="wifiGetAttrs",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def get_camera_custom_attributes(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac"]
		oneof = []
		valid = {
			"params": ["mac"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="getCustomAttrs",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def set_camera_custom_attributes(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac", "irLedMode"]
		oneof = []
		valid = {
			"params": ["mac", "irLedMode", "irLedLuminance", "mdMode", "mdThreshold", ="mdSensitivity", "mdWindowCoordinates", ]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="setCustomAttrs",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def purge_camera(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac"]
		oneof = []
		valid = {
			"params": ["mac"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="purgeCamera",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def get_camera_ptz_attributes(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac"]
		oneof = []
		valid = {
			"params": ["mac"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="ptzGetAttrs",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def camera_ptz_goto_home(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac"]
		oneof = []
		valid = {
			"params": ["mac"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="ptzGotoHome",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def camera_ptz_goto_absolute(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac", "pan", "tilt", "zoom"]
		oneof = []
		valid = {
			"params": ["mac", "pan", "tilt", "zoom"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="ptzGotoAbsolute",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	def camera_ptz_goto_relative(self, **kwargs):
		self.response = {}; payload = {}
		required = ["mac", "deltaPan", "deltaTilt", "deltaZoom"]
		oneof = []
		valid = {
			"params": ["mac", "deltaPan", "deltaTilt", "deltaZoom"]
		}
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hubsercomm(
				hub_address=self.iris.hub_address,
				method="ptzGotoRelative",
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)
import iris.payloads as payloads
import iris.request as request
import iris.utils as utils
from iris.devices.device import Device

class Hub(Device):
	def __init__(self, **kwargs):
		Device.__init__(self, **kwargs)
		self.namespace = "hub"

	def __hub_request(self, **kwargs):
		namespace = kwargs["namespace"]
		method = kwargs["method"]
		self.response = {}; payload = {}
		required, oneof, valid = utils.fetch_parameters(namespace, method, self.iris.validator)
		content = utils.process_parameters(opts=kwargs, required=required, oneof=oneof, valid=valid)
		if isinstance(content, dict):
			payload = payloads.hub_method(
				namespace=namespace,
				hub_address=self.iris.hub_address,
				method=method,
			)
			for k, v in content.items(): payload["payload"]["attributes"][k] = v
			request.send(client=self, payload=payload, debug=self.iris.debug)

	## hub ##
	def get_config(self, **kwargs):
		kwargs["namespace"] = "hub"
		kwargs["method"] = "GetConfig"
		self.__hub_request(**kwargs)

	def get_logs(self, **kwargs):
		kwargs["namespace"] = "hub"
		kwargs["method"] = "GetLogs"
		self.__hub_request(**kwargs)

	def pairing_request(self, **kwargs):
		kwargs["namespace"] = "hub"
		kwargs["method"] = "PairingRequest"
		self.__hub_request(**kwargs)

	def reset_log_level(self, **kwargs):
		kwargs["namespace"] = "hub"
		kwargs["method"] = "ResetLogLevel"
		self.__hub_request(**kwargs)

	def set_log_level(self, **kwargs):
		kwargs["namespace"] = "hub"
		kwargs["method"] = "SetLogLevel"
		self.__hub_request(**kwargs)

	def steam_logs(self, **kwargs):
		kwargs["namespace"] = "hub"
		kwargs["method"] = "StreamLogs"
		self.__hub_request(**kwargs)

	def unpairing_request(self, **kwargs):
		kwargs["namespace"] = "hub"
		kwargs["method"] = "UnpairingRequest"
		self.__hub_request(**kwargs)

	## hub4g ##
	def lte_get_info(self, **kwargs):
		kwargs["namespace"] = "hub4g"
		kwargs["method"] = "GetInfo"
		self.__hub_request(**kwargs)

	def lte_get_statistics(self, **kwargs):
		kwargs["namespace"] = "hub4g"
		kwargs["method"] = "GetStatistics"
		self.__hub_request(**kwargs)

	def lte_reset_statistics(self, **kwargs):
		kwargs["namespace"] = "hub4g"
		kwargs["method"] = "ResetStatistics"
		self.__hub_request(**kwargs)

	## hubadv ##
	def factory_reset(self, **kwargs):
		kwargs["namespace"] = "hubadv"
		kwargs["method"] = "FactoryReset"
		self.__hub_request(**kwargs)

	def firmware_update(self, **kwargs):
		kwargs["namespace"] = "hubadv"
		kwargs["method"] = "FirmwareUpdate"
		self.__hub_request(**kwargs)

	def get_device_info(self, **kwargs):
		kwargs["namespace"] = "hubadv"
		kwargs["method"] = "GetDeviceInfo"
		self.__hub_request(**kwargs)

	def get_known_devices(self, **kwargs):
		kwargs["namespace"] = "hubadv"
		kwargs["method"] = "GetKnownDevices"
		self.__hub_request(**kwargs)

	def reboot(self, **kwargs):
		kwargs["namespace"] = "hubadv"
		kwargs["method"] = "Reboot"
		self.__hub_request(**kwargs)

	def restart(self, **kwargs):
		kwargs["namespace"] = "hubadv"
		kwargs["method"] = "Restart"
		self.__hub_request(**kwargs)

	## hubalarm ##
	def alarm_activate(self, **kwargs):
		kwargs["namespace"] = "hubalarm"
		kwargs["method"] = "Activate"
		self.__hub_request(**kwargs)

	def alarm_arm(self, **kwargs):
		kwargs["namespace"] = "hubalarm"
		kwargs["method"] = "Arm"
		self.__hub_request(**kwargs)

	def alarm_clear_incident(self, **kwargs):
		kwargs["namespace"] = "hubalarm"
		kwargs["method"] = "ClearIncident"
		self.__hub_request(**kwargs)

	def alarm_disarm(self, **kwargs):
		kwargs["namespace"] = "hubalarm"
		kwargs["method"] = "Disarm"
		self.__hub_request(**kwargs)

	def alarm_panic(self, **kwargs):
		kwargs["namespace"] = "hubalarm"
		kwargs["method"] = "Panic"
		self.__hub_request(**kwargs)

	def alarm_suspend(self, **kwargs):
		kwargs["namespace"] = "hubalarm"
		kwargs["method"] = "Suspend"
		self.__hub_request(**kwargs)

	## hubbackup ##
	def backup(self, **kwargs):
		kwargs["namespace"] = "hubbackup"
		kwargs["method"] = "Backup"
		self.__hub_request(**kwargs)

	def restore(self, **kwargs):
		kwargs["namespace"] = "hubbackup"
		kwargs["method"] = "Restore"
		self.__hub_request(**kwargs)

	## hubchime ##
	def chime(self, **kwargs):
		kwargs["namespace"] = "hubchime"
		kwargs["method"] = "chime"
		self.__hub_request(**kwargs)

	## hubdebug ##
	def exec_process(self, **kwargs):
		kwargs["namespace"] = "hubdebug"
		kwargs["method"] = "ExecProcess"
		self.__hub_request(**kwargs)

	def get_agent_db(self, **kwargs):
		kwargs["namespace"] = "hubdebug"
		kwargs["method"] = "GetAgentDb"
		self.__hub_request(**kwargs)

	def get_bootlog(self, **kwargs):
		kwargs["namespace"] = "hubdebug"
		kwargs["method"] = "GetBootlog"
		self.__hub_request(**kwargs)

	def get_load(self, **kwargs):
		kwargs["namespace"] = "hubdebug"
		kwargs["method"] = "GetLoad"
		self.__hub_request(**kwargs)

	def get_processes(self, **kwargs):
		kwargs["namespace"] = "hubdebug"
		kwargs["method"] = "GetProcesses"
		self.__hub_request(**kwargs)

	def get_syslog(self, **kwargs):
		kwargs["namespace"] = "hubdebug"
		kwargs["method"] = "GetSyslog"
		self.__hub_request(**kwargs)

	## hubmetrics ##
	def end_metrics_job(self, **kwargs):
		kwargs["namespace"] = "hubmetrics"
		kwargs["method"] = "EndMetricsJob"
		self.__hub_request(**kwargs)

	def get_metrics_job_info(self, **kwargs):
		kwargs["namespace"] = "hubmetrics"
		kwargs["method"] = "GetMetricsJobInfo"
		self.__hub_request(**kwargs)

	def get_stored_metrics(self, **kwargs):
		kwargs["namespace"] = "hubmetrics"
		kwargs["method"] = "GetStoredMetrics"
		self.__hub_request(**kwargs)

	def list_metrics(self, **kwargs):
		kwargs["namespace"] = "hubmetrics"
		kwargs["method"] = "GetMetricsJobInfo"
		self.__hub_request(**kwargs)

	def start_metrics_job(self, **kwargs):
		kwargs["namespace"] = "hubmetrics"
		kwargs["method"] = "StartMetricsJob"
		self.__hub_request(**kwargs)

	## hubnetwork ##
	def get_routing_table(self, **kwargs):
		# Message type [hubnet:GetRoutingTable] is not supported
		kwargs["namespace"] = "hubnetwork"
		kwargs["method"] = "GetRoutingTable"
		self.__hub_request(**kwargs)

	## hubsercomm ##
	def get_camera_password(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "getCameraPassword"
		self.__hub_request(**kwargs)

	def pair_camera(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "pair"
		self.__hub_request(**kwargs)

	def factory_reset_camera(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "reset"
		self.__hub_request(**kwargs)

	def reboot_camera(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "reboot"
		self.__hub_request(**kwargs)

	def configure_camera(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "config"
		self.__hub_request(**kwargs)

	def upgrade_camera_firmware(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "upgrade"
		self.__hub_request(**kwargs)

	def get_camera_state(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "getState"
		self.__hub_request(**kwargs)

	def get_camera_version(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "getVersion"
		self.__hub_request(**kwargs)

	def get_camera_day_night_setting(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "getDayNight"
		self.__hub_request(**kwargs)

	def get_camera_ipv4(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "getIPAddress"
		self.__hub_request(**kwargs)

	def get_camera_model(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "getModel"
		self.__hub_request(**kwargs)

	def get_camera_info(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "getInfo"
		self.__hub_request(**kwargs)

	def get_camera_attributes(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "getAttrs"
		self.__hub_request(**kwargs)

	def start_camera_motion_detection(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "motionDetectStart"
		self.__hub_request(**kwargs)

	def stop_camera_motion_detection(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "motionDetectStop"
		self.__hub_request(**kwargs)

	def start_camera_video_stream(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "videoStreamStart"
		self.__hub_request(**kwargs)

	def stop_camera_video_stream(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "videoStreamStop"
		self.__hub_request(**kwargs)

	def start_camera_wifi_scan(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "wifiScanStart"
		self.__hub_request(**kwargs)

	def end_camera_wifi_scan(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "wifiScanEnd"
		self.__hub_request(**kwargs)

	def camera_wifi_connect(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "wifiConnect"
		self.__hub_request(**kwargs)

	def camera_wifi_disconnect(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "wifiDisconnect"
		self.__hub_request(**kwargs)

	def camera_get_wifi_attributes(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "wifiGetAttrs"
		self.__hub_request(**kwargs)

	def get_camera_custom_attributes(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "getCustomAttrs"
		self.__hub_request(**kwargs)

	def set_camera_custom_attributes(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "setCustomAttrs"
		self.__hub_request(**kwargs)

	def purge_camera(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "purgeCamera"
		self.__hub_request(**kwargs)

	def get_camera_ptz_attributes(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "ptzGetAttrs"
		self.__hub_request(**kwargs)

	def camera_ptz_goto_home(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "ptzGotoHome"
		self.__hub_request(**kwargs)

	def camera_ptz_goto_absolute(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "ptzGotoAbsolute"
		self.__hub_request(**kwargs)

	def camera_ptz_goto_relative(self, **kwargs):
		kwargs["namespace"] = "hubsercomm"
		kwargs["method"] = "ptzGotoRelative"
		self.__hub_request(**kwargs)

	## hubsounds ##
	def play_url(self, **kwargs):
		kwargs["namespace"] = "hubsounds"
		kwargs["method"] = "PlayURL"
		self.__hub_request(**kwargs)

	def play_tone(self, **kwargs):
		kwargs["namespace"] = "hubsounds"
		kwargs["method"] = "PlayTone"
		self.__hub_request(**kwargs)

	## hubzigbee ##
	def reset_zigbee_chip(self, **kwargs):
		kwargs["namespace"] = "hubzigbee"
		kwargs["method"] = "Reset"
		self.__hub_request(**kwargs)

	def zigbee_scan(self, **kwargs):
		kwargs["namespace"] = "hubzigbee"
		kwargs["method"] = "Scan"
		self.__hub_request(**kwargs)

	def get_zigbee_config(self, **kwargs):
		kwargs["namespace"] = "hubzigbee"
		kwargs["method"] = "GetConfig"
		self.__hub_request(**kwargs)

	## hubzwave ##
	def reset_zwave_chip(self, **kwargs):
		kwargs["namespace"] = "hubzwave"
		kwargs["method"] = "Reset"
		self.__hub_request(**kwargs)

	def zwave_force_primary(self, **kwargs):
		kwargs["namespace"] = "hubzwave"
		kwargs["method"] = "ForcePrimary"
		self.__hub_request(**kwargs)

	def zwave_force_secondary(self, **kwargs):
		kwargs["namespace"] = "hubzwave"
		kwargs["method"] = "ForceSecondary"
		self.__hub_request(**kwargs)

	def zwave_network_info(self, **kwargs):
		kwargs["namespace"] = "hubzwave"
		kwargs["method"] = "NetworkInformation"
		self.__hub_request(**kwargs)

	def zwave_network_heal(self, **kwargs):
		kwargs["namespace"] = "hubzwave"
		kwargs["method"] = "Heal"
		self.__hub_request(**kwargs)

	def zwave_cancel_network_heal(self, **kwargs):
		kwargs["namespace"] = "hubzwave"
		kwargs["method"] = "CancelHeal"
		self.__hub_request(**kwargs)

	def zwave_remove_zombie(self, **kwargs):
		kwargs["namespace"] = "hubzwave"
		kwargs["method"] = "RemoveZombie"
		self.__hub_request(**kwargs)

	def zwave_associate(self, **kwargs):
		kwargs["namespace"] = "hubzwave"
		kwargs["method"] = "Associate"
		self.__hub_request(**kwargs)

	def zwave_assign_return_routes(self, **kwargs):
		kwargs["namespace"] = "hubzwave"
		kwargs["method"] = "AssignReturnRoutes"
		self.__hub_request(**kwargs)
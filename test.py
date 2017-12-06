#!/usr/bin/env python3

from iris.core import Iris
from iris.devices.switch import Switch
from iris.devices.thermostat import Thermostat
from iris.devices.doorlock import DoorLock
from pprint import pprint

iris = Iris(
	profile="MyHome",
	debug=False
)

s = Switch(iris=iris)
print(s.namespace)
#pprint(s.iris.devices)
#pprint(s.iris.ws)

#iris.battery_states()
#iris.find_device()
#iris.get_hub()
#iris.get_device(device="Upstairs")
#therm = Thermostat(iris=iris)
#therm.set_hvacmode(device="Downstairs", mode="COOL")
#therm.set_coolsetpoint(device="Downstairs", setpoint=68)
#pprint(iris.devices)
#iris.list_devices()
#iris.show_history(limit=10)
#iris.list_rules()
#iris.list_scenes()
#iris.light_on(device_id="b8028f27-717d-45d4-94ee-111154645715")
#iris.light_off(device="Entry Way Smart Plug")
#iris.light_on(device="Entry Way Smart Plug")
##iris.unlock_door(device="Front Door")
#iris.hub_chime()
#pprint(iris.response)

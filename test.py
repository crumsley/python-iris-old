#!/usr/bin/env python3

from iris.core import Iris
from iris.account import Account
from iris.devices.switch import Switch
from iris.devices.thermostat import Thermostat
from iris.devices.doorlock import DoorLock
from iris.person import Person
from iris.hub import Hub
from pprint import pprint

iris = Iris(
	profile="MyHome",
	debug=True
)

h = Hub(iris=iris)
#h.get_logs()
#h.get_processes()
#h.get_known_devices()
#h.get_device_info()
#h.list_hubs()
#h.get_syslog()
#h.chime()
#h.pairing_request()
#h.reset_log_level()
#h.backup()
#pprint(h.response)

#a = Account(iris=iris)
#a.list_adjustments()
#a.list_devices()
#a.list_hubs()
#a.list_invoices()
#a.list_places()
#pprint(a.response)


name = ""

#p = Person(iris=iris)
#p.list_persons()
#p.list_history_entries(name=name)
#p.get_security_answers(name=name)
#print(p.success)
#pprint(p.response)
#s.foo()
#pprint(s.response)
#print(iris.hub_id)
#pprint(s.iris.devices)
#pprint(s.iris.ws)
#pprint(iris.persons)
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

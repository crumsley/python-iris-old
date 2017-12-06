devices = {
	"dimmer": {
		"brightness": {
			"type": int,
			"readwrite": "rw",
			"min": 0,
			"max": 100,
		},
	},
	"doorlock": {
		"lockstate": {
			"type": str,
			"readwrite": "rw",
			"valid": ["LOCKED", "UNLOCKED", "LOCKING", "UNLOCKING"]
		},
	},
	"halo": {
		"room": {
			"type": str,
			"readwrite": "rw",
			"valid": ["NONE", "BASEMENT", "BEDROOM", "DEN", "DINING_ROOM", "DOWNSTAIRS", "ENTRYWAY", "FAMILY_ROOM", "GAME_ROOM", "GUEST_BEDROOM", "HALLWAY", "KIDS_BEDROOM", "LIVING_ROOM", "MASTER_BEDROOM", "OFFICE,STUDY", "UPSTAIRS", "WORKOUT_ROOM"]
		},
		"haloalertstate": {
			"type": str,
			"readwrite": "rw",
			"valid": ["QUIET", "INTRUDER", "PANIC", "WATER", "SMOKE", "CO", "CARE", "ALERTING_GENERIC"]
		},
	},
	"swit": {
		"state": {
			"type": str,
			"readwrite": "rw",
			"valid": ["OFF", "ON"],
		},
		"inverted": {
			"type": bool,
			"readwrite": "rw",
		},	
	},
	"therm": {
		"coolsetpoint": {
			"type": int,
			"readwrite": "rw",
		},
		"heatsetpoint": {
			"type": int,
			"readwrite": "rw",
		},
		"hvacmode": {
			"type": str,
			"readwrite": "rw",
			"valid": ["OFF", "AUTO", "COOL", "HEAT", "ECO"],
		},
		"fanmode": {
			"type": int,
			"readwrite": "rw",
			"min": 0,
			"max": 7
		},
		"emergencyheat": {
			"type": str,
			"readwrite": "rw",
			"valid": ["ON", "OFF"]
		},
		"controlmode": {
			"type": str,
			"readwrite": "rw",
			"valid": ["PRESENCE", "MANUAL", "SCHEDULESIMPLE", "SCHEDULEADVANCED"],
		},
		"filterlifespanruntime": {
			"type": int,
			"readwrite": "rw",
		},
		"filterlifespandays": {
			"type": int,
			"readwrite": "rw",
		}
	}
}

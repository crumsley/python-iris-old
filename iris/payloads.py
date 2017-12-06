# https://github.com/thegillion/Iris-Web-Portal/blob/master/powerhouse.js
import json

def set_active_place(place_id=None):
	return json.dumps({
		"type": "sess:SetActivePlace",
		"headers": {
			"destination":"SERV:sess:",
			"correlationId": "78f7d29a-222e-4976-9d2b-d1f553cf8881",
			"isRequest" :True
		},
		"payload": {
			"messageType": "sess:SetActivePlace",
			"attributes": {
				"placeId": place_id
			}
		}
	})

def get_attributes(device_id=None, namespace=None, key=None):
	return json.dumps({
		"type": "base:GetAttributes",
		"headers": {
			"destination": "DRIV:dev:{}".format(device_id),
			"correlationId": "74cb2fe5-3c80-4294-bf36-e6a6a5faf08a",
			"isRequest": True
		},
		"payload":{
			"messageType": "base:GetAttributes",
			"attributes": {
				namespace: key,
			}
		}
	})

def set_attributes(place_id: None, device_id: None, namespace: None, key: None, value: None):
	return json.dumps({
		"type": "base:SetAttributes",
		"headers": {
			#"destination": "DRIV:dev:' + devIDlist[(ID - 1)] + '",
			"destination": "DRIV:dev:{}".format(device_id),
			"correlationId": "790525f5-171f-4533-a952-0dcafb9b5310",
			"isRequest": True
		},
		"payload": {
			"messageType": "base:SetAttributes",
			"attributes": {
				"{}:{}".format(namespace, key): value
			}
		}
	})

def person(address=None, method=None, namespace=None):
	return json.dumps({
		"type": "person:{}".format(method),
		"headers": {
			#"destination": "SERV:person:{}".format(person_id),
			"destination": address,
			"correlationId": "78cd5c7c-f5f7-4dba-9032-99ad183e64be",
			"isRequest": True
		},
		"payload": {
			"messageType": "{}:{}".format(namespace, method),
			"attributes": {}
		}
	})

def place(place_id=None, method=None):
	return json.dumps({
		"type": "place:{}".format(method),
		"headers": {
			"destination": "SERV:place:{}".format(place_id),
			"correlationId": "78cd5c7c-f5f7-4dba-9032-99ad183e64be",
			"isRequest": True
		},
		"payload": {
			"messageType": "place:{}".format(method),
			"attributes": {}
		}
	})



# Deprecated
def hub_chime(place_id=None):
	return json.dumps({
		"type": "place:HubChime",
		"headers": {
			"destination": "SERV:place:{}".format(place_id),
			"correlationId": "68c97150-d5d2-4717-ae94-bf9e2457ed5d",
			"isRequest": True
		},
		"payload": {
			"messageType": "place:HubChime",
			"attributes": {}
		}
	})

def list_scenes(place_id=None):
	return json.dumps({
		"type": "scene:ListScenes",
		"headers": {
			"destination": "SERV:scene:",
			"correlationId": "68c97150-d5d2-4717-ae94-bf9e2457ed5d",
			"isRequest": True
		},
		"payload": {
			"messageType": "scene:ListScenes",
			"attributes": {
				"placeId": place_id
			}
		}
	})

def list_rules(place_id=None):
	return json.dumps({
		"type": "rule:ListRules",
		"headers": {
			"destination":"SERV:rule:",
			"correlationId": "90704a94-ba52-4252-816b-e5680e7999a0",
			"isRequest": True
		},
		"payload": {
			"messageType": "rule:ListRules",
			"attributes": {
				"placeId": place_id
			}
		}
	})


def system_log(place_id=None):
	return json.dumps({
		"type": "sess:SetActivePlace",
		"headers": {
			"destination": "SERV:sess:",
			"correlationId": "78f7d29a-222e-4976-9d2b-d1f553cf8881",
			"isRequest": True
		},
		"payload":{
			"messageType": "sess:SetActivePlace",
			"attributes": {
				#"placeId":"' + placeID + '"
				"placeId": " {} ".format(place_id)
			}
		}
	})

def send_remove(symbol=None):
	return json.dumps({
		"command": "remove",
		"tickerSymbol": " {} ".format(symbol)
	})
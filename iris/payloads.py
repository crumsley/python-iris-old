def set_active_place(place_id=None):
	return {
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
	}

def get_attributes(device_id=None, namespace=None, key=None):
	return {
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
	}

def set_attributes(place_id: None, device_id: None, namespace: None, key: None, value: None):
	return {
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
	}

def account_method(account_id=None, method=None, namespace=None):
	return {
		"type": "{}:{}".format(namespace, method),
		"headers": {
			"destination": "SERV:account:{}".format(account_id),
			"correlationId": "78cd5c7c-f5f7-4dba-9032-99ad183e64be",
			"isRequest": True
		},
		"payload": {
			"messageType": "{}:{}".format(namespace, method),
			"attributes": {}
		}
	}

def hub_method(hub_address=None, method=None, namespace=None):
	return {
		"type": "{}:{}".format(namespace, method),
		"headers": {
			"destination": hub_address,
			"correlationId": "78cd5c7c-f5f7-4dba-9032-99ad183e64be",
			"isRequest": True
		},
		"payload": {
			"messageType": "{}:{}".format(namespace, method),
			"attributes": {}
		}
	}

def keypad_method(place_id=None, method=None, namespace=None):
	return {
		"type": "{}:{}".format(namespace, method),
		"headers": {
			"destination": hub_address,
			"correlationId": "78cd5c7c-f5f7-4dba-9032-99ad183e64be",
			"isRequest": True
		},
		"payload": {
			"messageType": "{}:{}".format(namespace, method),
			"attributes": {}
		}
	}

def person(person_id=None, method=None, namespace=None):
	return {
		"type": "{}:{}".format(namespace, method),
		"headers": {
			"destination": "SERV:{}:{}".format(namespace, person_id),
			"correlationId": "78cd5c7c-f5f7-4dba-9032-99ad183e64be",
			"isRequest": True
		},
		"payload": {
			"messageType": "{}:{}".format(namespace, method),
			"attributes": {}
		}
	}

def place(place_id=None, method=None):
	return {
		"type": "place:{}".format(method),
		"headers": {
			"destination": "SERV:place:{}".format(place_id),
			"correlationId": "79cd5c7c-f5f7-4dba-9032-99ad183e64be",
			"isRequest": True
		},
		"payload": {
			"messageType": "place:{}".format(method),
			"attributes": {}
		}
	}

def therm_method(device_address=None, method=None, namespace=None):
	return {
		"type": "{}:{}".format(namespace, method),
		"headers": {
		"destination": device_address,
			#"destination": "DRIV:dev:{}".format(device_id),
			"correlationId": "78cd5c7c-f5f7-4dba-9032-99ad183e64be",
			"isRequest": True
		},
		"payload": {
			"messageType": "{}:{}".format(namespace, method),
			"attributes": {}
		}
	}

# Deprecated
# def hub_chime(place_id=None):
# 	return {
# 		"type": "place:HubChime",
# 		"headers": {
# 			"destination": "SERV:place:{}".format(place_id),
# 			"correlationId": "68c97150-d5d2-4717-ae94-bf9e2457ed5d",
# 			"isRequest": True
# 		},
# 		"payload": {
# 			"messageType": "place:HubChime",
# 			"attributes": {}
# 		}
# 	}

# def list_scenes(place_id=None):
# 	return {
# 		"type": "scene:ListScenes",
# 		"headers": {
# 			"destination": "SERV:scene:",
# 			"correlationId": "68c97150-d5d2-4717-ae94-bf9e2457ed5d",
# 			"isRequest": True
# 		},
# 		"payload": {
# 			"messageType": "scene:ListScenes",
# 			"attributes": {
# 				"placeId": place_id
# 			}
# 		}
# 	}

# def list_rules(place_id=None):
# 	return {
# 		"type": "rule:ListRules",
# 		"headers": {
# 			"destination":"SERV:rule:",
# 			"correlationId": "90704a94-ba52-4252-816b-e5680e7999a0",
# 			"isRequest": True
# 		},
# 		"payload": {
# 			"messageType": "rule:ListRules",
# 			"attributes": {
# 				"placeId": place_id
# 			}
# 		}
# 	}


# def system_log(place_id=None):
# 	return {
# 		"type": "sess:SetActivePlace",
# 		"headers": {
# 			"destination": "SERV:sess:",
# 			"correlationId": "78f7d29a-222e-4976-9d2b-d1f553cf8881",
# 			"isRequest": True
# 		},
# 		"payload":{
# 			"messageType": "sess:SetActivePlace",
# 			"attributes": {
# 				#"placeId":"' + placeID + '"
# 				"placeId": " {} ".format(place_id)
# 			}
# 		}
# 	}

# def send_remove(symbol=None):
# 	return {
# 		"command": "remove",
# 		"tickerSymbol": " {} ".format(symbol)
# 	}
#!/usr/bin/env python3

import json
import os
import re
import sys
import xmltodict
from pprint import pprint

parameters = {}

files = [f for f in os.listdir(".") if os.path.isfile(f)]
for filename in files:
	is_device = False
	is_person = False
	is_place = False

	if filename.endswith('.xml'):
		xml = None
		contents = open(filename, "r").read()
		try:
			xml = dict(xmltodict.parse(contents))
		except:
			print("{} does not appear to be a valid XML file. Ignoring.".format(filename))

		if xml:
			attributes = []
			methods = []
			events = []
			if "@enhances" in xml["c:capability"] and xml["c:capability"]["@enhances"].lower() == "device":
				is_device = True
				
			if "@namespace" in xml["c:capability"]:
				namespace = xml["c:capability"]["@namespace"]
				if namespace == "person": is_person = True
				if namespace == "place": is_place = True

				if "c:attributes" in xml["c:capability"]:
					if isinstance(xml["c:capability"]["c:attributes"], dict):
						if "c:attribute" in xml["c:capability"]["c:attributes"]:
							if isinstance(xml["c:capability"]["c:attributes"]["c:attribute"], dict):
								attributes.append(xml["c:capability"]["c:attributes"]["c:attribute"])
							elif isinstance(xml["c:capability"]["c:attributes"]["c:attribute"], list):
								attributes = xml["c:capability"]["c:attributes"]["c:attribute"]

				if "c:methods" in xml["c:capability"]:
					if isinstance(xml["c:capability"]["c:methods"], dict):
						if "c:method" in xml["c:capability"]["c:methods"]:
							if isinstance(xml["c:capability"]["c:methods"]["c:method"], dict):
								methods.append(xml["c:capability"]["c:methods"]["c:method"])
							elif isinstance(xml["c:capability"]["c:methods"]["c:method"], list):
								methods = xml["c:capability"]["c:methods"]["c:method"]

				if "c:events" in xml["c:capability"]:
					if isinstance(xml["c:capability"]["c:events"], dict):
						if "c:event" in xml["c:capability"]["c:events"]:
							if isinstance(xml["c:capability"]["c:events"]["c:event"], dict):
								events.append(xml["c:capability"]["c:events"]["c:event"])
							elif isinstance(xml["c:capability"]["c:events"]["c:event"], list):
								events = xml["c:capability"]["c:events"]["c:event"]

			if len(methods) > 0 or len(attributes) > 0 or len(events) > 0:
				parameters[namespace] = {}

			if len(attributes) > 0:
				parameters[namespace]["attributes"] = {}
				for attribute in attributes:
					attribute_name = attribute["@name"]
					parameters[namespace]["attributes"][attribute_name] = {}
					if "@readwrite" in attribute:
						parameters[namespace]["attributes"][attribute_name]["readonly"] = False if attribute["@readwrite"] == "rw" else True
					if "@optional" in attribute:
						parameters[namespace]["attributes"][attribute_name]["required"] = False if attribute["@optional"] == "true" else True
					if "@required" in attribute:
						parameters[namespace]["attributes"][attribute_name]["required"] = True if attribute["@required"] == "true" else False
					if "@type" in attribute:
						parameters[namespace]["attributes"][attribute_name]["type"] = attribute["@type"]
					if "@description" in attribute:
						parameters[namespace]["attributes"][attribute_name]["description"] = attribute["@description"]
					if "@min" in attribute:
						parameters[namespace]["attributes"][attribute_name]["min"] = attribute["@min"]
					if "@max" in attribute:
						parameters[namespace]["attributes"][attribute_name]["max"] = attribute["@max"]
					if "@values" in attribute:
						parameters[namespace]["attributes"][attribute_name]["valid"] = re.split("\s*,\s*", attribute["@values"])

			if len(methods) > 0:
				parameters[namespace]["methods"] = {}
				for method in methods:
					method_name = method["@name"]
					parameters[namespace]["methods"][method_name] = {
					 	"required": [],
					 	"oneof": [],
					 	"valid": {
					 		"params": {}
					 	}
					}

					if is_device == True:
						parameters[namespace]["methods"][method_name]["oneof"].append(["device_name", "device_id"])
						parameters[namespace]["methods"][method_name]["valid"]["params"]["device_name"] = {
							"type": "string",
							"decription": "The name of the {} device.".format(namespace)
						}
						parameters[namespace]["methods"][method_name]["valid"]["params"]["device_id"] = {
							"type": "uuid",
							"decription": "The ID of the {} device.".format(namespace)
						}

					if is_person == True:
						parameters[namespace]["methods"][method_name]["oneof"].append(["person_name", "person_id"])
						parameters[namespace]["methods"][method_name]["valid"]["params"]["person_name"] = {
							"type": "string",
							"decription": "The name of the {}.".format(namespace)
						}
						parameters[namespace]["methods"][method_name]["valid"]["params"]["person_id"] = {
							"type": "uuid",
							"decription": "The ID of the {}.".format(namespace)
						}

					if "c:parameters" in method:
						if isinstance(method["c:parameters"], dict):
				 			if "c:parameter" in method["c:parameters"]:
				 				method_parameters = []
				 				if isinstance(method["c:parameters"]["c:parameter"], dict):
				 					method_parameters.append(method["c:parameters"]["c:parameter"])
						 		elif isinstance(method["c:parameters"]["c:parameter"], list):
						 			method_parameters = method["c:parameters"]["c:parameter"]
						 		for p in method_parameters:
						 			p_name = p["@name"]
						 			p_type = p["@type"]

						 			if "@optional" in p:
						 				p["@optional"] = True if p["@optional"] == "true" else False

						 			if "@required" in p:
						 				p["@optional"] = False if p["@required"] == "true" else False

						 			parameters[namespace]["methods"][method_name]["valid"]["params"][p_name] = {"type": p_type}
						 			if "@description" in p: parameters[namespace]["methods"][method_name]["valid"]["params"][p_name]["description"] = p["@description"]
						 			if "@optional" in p: parameters[namespace]["methods"][method_name]["valid"]["params"][p_name]["optional"] = p["@optional"]
						 			if "@min" in p: parameters[namespace]["methods"][method_name]["valid"]["params"][p_name]["min"] = p["@min"]
						 			if "@max" in p: parameters[namespace]["methods"][method_name]["valid"]["params"][p_name]["max"] = p["@max"]
						 			

						 			if "@optional" in p:
						 				if p["@optional"] == False:
						 					parameters[namespace]["methods"][method_name]["required"].append(p_name)

						 			if "@values" in p:
						 				parameters[namespace]["methods"][method_name]["valid"][p_name] = re.split("\s*,\s*", p["@values"])

			if len(events) > 0:
				parameters[namespace]["events"] = {}
				for event in events:
					event_name = event["@name"]
					parameters[namespace]["events"][event_name] = {
					 	"required": [],
					 	"valid": {
					 		"params": {}
					 	}
					}
					if "@description" in event:
						parameters[namespace]["events"][event_name]["description"] = event["@description"]
					if "c:parameters" in event:
						if "c:parameter" in event["c:parameters"]:
							event_parameters = []
							if isinstance(event["c:parameters"]["c:parameter"], dict):
								event_parameters.append(event["c:parameters"]["c:parameter"])
							elif isinstance(event["c:parameters"]["c:parameter"], list):
								event_parameters = event["c:parameters"]["c:parameter"]

							if len(event_parameters) > 0:
								for p in event_parameters:
									p_name = p["@name"]
									p_type = p["@type"]

									if "@optional" in p:
										p["@optional"] = True if p["@optional"] == "true" else False

									if "required" in p:
										p["@optional"] = False if p["@required"] == "true" else False

									parameters[namespace]["events"][event_name]["valid"]["params"][p_name] = {"type": p_type}
									if "@description" in p: parameters[namespace]["events"][event_name]["valid"]["params"][p_name]["description"] = p["@description"]
									if "@optional" in p: parameters[namespace]["events"][event_name]["valid"]["params"][p_name]["optional"] = p["@optional"]
									if "@min" in p: parameters[namespace]["events"][event_name]["valid"]["params"][p_name]["min"] = p["@min"]
									if "@max" in p: parameters[namespace]["events"][event_name]["valid"]["params"][p_name]["max"] = p["@max"]
									

									if "@optional" in p:
										if p["@optional"] == False:
											parameters[namespace]["events"][event_name]["required"].append(p_name)

									if "@values" in p:
										parameters[namespace]["events"][event_name]["valid"]["params"][p_name] = re.split("\s*,\s*", p["@values"])

print(json.dumps(parameters, indent=4))

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
	if filename.endswith('.xml'):
		xml = None
		contents = open(filename, "r").read()
		try:
			xml = dict(xmltodict.parse(contents))
		except:
			print("{} does not appear to be a valid XML file. Ignoring.".format(filename))

		if xml:
			methods = []
			if "@namespace" in xml["c:capability"]:
				namespace = xml["c:capability"]["@namespace"]
				if "c:methods" in xml["c:capability"]:
					if isinstance(xml["c:capability"]["c:methods"], dict):
						if "c:method" in xml["c:capability"]["c:methods"]:
							if isinstance(xml["c:capability"]["c:methods"]["c:method"], dict):
								methods.append(xml["c:capability"]["c:methods"]["c:method"])
							elif isinstance(xml["c:capability"]["c:methods"]["c:method"], list):
								methods = xml["c:capability"]["c:methods"]["c:method"]


			if len(methods) > 0:
				parameters[namespace] = {"methods": {}}
				for method in methods:
					method_name = method["@name"]
					parameters[namespace]["methods"][method_name] = {
					 	"required": [],
					 	"valid": {
					 		"params": {}
					 	}
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
						 			print("{}: {}: {} is a {}".format(filename, method_name, p_name, p_type))
						 			print("")

						 			if "@optional" in p:
						 				p["@optional"] = True if p["@optional"] == "true" else False

						 			parameters[namespace]["methods"][method_name]["valid"]["params"][p_name] = {"type": p_type}
						 			if "@description" in p: parameters[namespace]["methods"][method_name]["valid"]["params"][p_name]["description"] = p["@description"]
						 			if "@optional" in p: parameters[namespace]["methods"][method_name]["valid"]["params"][p_name]["optional"] = p["@optional"]
						 			if "@min" in p: parameters[namespace]["methods"][method_name]["valid"]["params"][p_name]["min"] = int(p["@min"])
						 			if "@max" in p: parameters[namespace]["methods"][method_name]["valid"]["params"][p_name]["max"] = int(p["@max"])
						 			

						 			if "@optional" in p:
						 				if p["@optional"] == "false":
						 					parameters[namespace]["methods"][method_name]["required"].append(p["@name"])

						 			if "@values" in p:
						 				parameters[namespace]["methods"][method_name]["valid"][p["@name"]] = re.split("\s*,\s*", p["@values"])

#pprint(parameters)
#print(json.dumps(parameters))
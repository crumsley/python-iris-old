import iris.attributes as attributes
import iris.exception as exception
import iris.payloads as payloads
import iris.request as request
import iris.utils as utils
from pprint import pprint

class Device(object):
	def __init__(self, **kwargs):
		self.success = None
		self.response = {}

		if "iris" in kwargs:
			self.iris = kwargs["iris"]
		else:
			raise exception.MissingConstructorParameter(parameter="iris")

		if not str(type(self.iris)) == "<class 'iris.core.Iris'>":
			raise exception.NotAnIrisCoreObject(class_name=str(type(self)))

		self.ws = self.iris.ws

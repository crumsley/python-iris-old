import iris.exception as exception

class Device(object):
	def __init__(self, **kwargs):
		self.success = None
		self.response = {}

		if "iris" in kwargs:
			self.iris = kwargs["iris"]
		else:
			raise exception.MissingConstructorParameter(parameter="iris")

		if str(type(self.iris)) == "<class 'iris.core.Iris'>":
			self.ws = self.iris.ws
		else:
			raise exception.NotAnIrisCoreObject(class_name=str(type(self)))

import os
from setuptools import setup, find_packages

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name = "iris",
	version = "0.1.0",
	author = "Gary Danko",
	author_email = "gdanko@gmail.com",
	url = "https://github.com/gdanko/python-iris",
	license = "GPLv3",
	description = "A Python based SDK for the Lowe's Iris 2nd generation API",
	packages = ["iris", "iris/devices"],
	package_dir = {"iris": "iris", "devices": "iris/devices"},
	install_requires = ["requests", "websocket-client"],
	#scripts = ["scripts/iris"],

	# See https://pypi.python.org/pypi?%3Aaction=list_classifiers
	classifiers = [
		"Development Status :: 4 - Beta",
		"Environment :: Console",
		"Intended Audience :: System Administrators",
		"License :: Other/Proprietary License",
		"Operating System :: POSIX :: Other",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.3",
		"Programming Language :: Python :: 3.4",
		"Programming Language :: Python :: 3.5"
	]
)


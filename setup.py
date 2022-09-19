from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in kenya_vat/__init__.py
from kenya_vat import __version__ as version

setup(
	name="kenya_vat",
	version=version,
	description="An app for the region Kenya",
	author="HTS Qatar",
	author_email="rafi@htsqatar.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

from setuptools import setup, find_packages
import json

install_requires = []

with open('Pipfile.lock') as fd:
    lock_data = json.load(fd)
    install_requires = install_requires + [
        package_name + package_data['version']
        for package_name, package_data in lock_data['default'].items()
    ]
    install_requires = install_requires + [
        package_name + package_data['version']
        for package_name, package_data in lock_data['develop'].items()
    ]

setup(name='myservice',
      version="0.1",
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      install_requires=install_requires)

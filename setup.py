from distutils.core import setup

with open('requirements.txt') as file:
    dependencies = file.read().splitlines()

setup(
    name='Quick API Tester',
    install_requires=dependencies
)

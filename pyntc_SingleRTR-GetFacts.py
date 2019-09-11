#pyntc is an open source multi-vendor Python library that establishes a common framework for working with different network APIs & device types (including IOS devices)
#
#It's main purpose to is to simplify the execution of common tasks including:
#
#Executing commands
#Copying files
#Upgrading devices
#Rebooting devices
#Saving / Backing Up Configs
#pyntc currently supports four device types:
#
#cisco_ios_ssh
#cisco_nxos_nxapi
#arista_eos_eapi
#juniper_junos_netconf
#https://github.com/networktocode/pyntc

import json
from pyntc import ntc_device as NTC
rtr = NTC(host='192.168.122.26', username='cisco', password='cisco', device_type='cisco_ios_ssh')
rtr.open()

ios_output = rtr.facts
print (json.dumps(ios_output, indent=4))

rtr.config_list([' hostname mgmt_python'])


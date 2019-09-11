
#!/usr/bin/env python

import json
from pyntc import ntc_device as NTC

rtr = NTC(host='192.168.122.26', username='cisco', password='cisco', device_type='cisco_ios_ssh')
rtr.open()

ios_output = rtr.facts
print (json.dumps(ios_output, indent=4))

rtr.config_list(['router ospf 1', 
                 'no network 0.0.0.0 255.255.255.255 area 0', 
                 'network 10.2.2.1 255.255.255.255 area 0', 
                 'network 192.168.122.0 255.255.255.0 area 0',
                 'network 10.3.3.1 255.255.255.255 area 0'])
                 
rtr.close()
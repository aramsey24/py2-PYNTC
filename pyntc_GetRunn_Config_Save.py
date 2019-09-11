#this script captures the running config and saves the file

#two methods of writing code to get the running config:
#1st method

#!/usr/bin/env python

import json
from pyntc import ntc_device as NTC

rtr = NTC(host='192.168.122.26', username='cisco', password='cisco', device_type='cisco_ios_ssh')
rtr.open()

ios_run = rtr.running_config
#comment out the below line if you don't want output seen on the screen while running script.
print (ios_run)

HOST = '192.168.122.26'
saveoutput = open('Running-CFG' + HOST, 'w')
saveoutput.write(ios_run)
saveoutput.close

rtr.close()


#2nd method-less code, 5 lines of code!


#!/usr/bin/env python

#!/usr/bin/env python

import json
from pyntc import ntc_device as NTC

rtr = NTC(host='192.168.122.26', username='cisco', password='cisco', device_type='cisco_ios_ssh')
rtr.open()

ios_run = rtr.backup_running_config('switchbackup.cfg')
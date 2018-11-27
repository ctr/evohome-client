#!/usr/bin/python

from evohomeclient2 import EvohomeClient
import time
import sys

import datetime
currenttime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
print "Current time is: " + currenttime

client = EvohomeClient('christopher.rodgers@cardiov.ox.ac.uk', 'toasty2015Y')

client.zone_schedules_backup('evohome_backup' + currenttime + '.json')

print "Backup complete"


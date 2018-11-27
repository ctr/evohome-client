#!/usr/bin/python

from evohomeclient2 import EvohomeClient
import time
import sys

import datetime
print datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

client = EvohomeClient('christopher.rodgers@cardiov.ox.ac.uk', 'toasty2015Y')

for device in client.temperatures():
    print device["name"]

while True:
    time.sleep(60)
    for device in client.temperatures():
        sys.stdout.write( device["name"] )
	sys.stdout.write( ", " )
    sys.stdout.write( "\n" )



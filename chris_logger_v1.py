#!/usr/bin/python

# Log the 8 Horn Lane Evohome temperatures regularly

from evohomeclient2 import EvohomeClient
import time
import sys
import datetime

# Connect to Honeywell servers
client = EvohomeClient('christopher.rodgers@cardiov.ox.ac.uk', 'toasty2015Y')

# Open log file
f = open("evohome_log.csv","a+",buffering=1)

f.write("\n\nNew logging session at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ".\nDevice_list,")

first = True
for device in client.temperatures():
    if first:
        first = False
    else:
        f.write(",")
    f.write(device["name"] + "_setpoint," + device["name"] + "_temp")
f.write("\n")
    
while True:
    time.sleep(30)
    f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+",")
    sys.stdout.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+",")

    try:
        first = True
        for device in client.temperatures():
            if first:
                first = False
            else:
                f.write(",")
                sys.stdout.write(",")

            f.write(str(device["setpoint"]) + "," + str(device["temp"]))
            sys.stdout.write(str(device["setpoint"]) + "," + str(device["temp"]))
    except Exception as err:
        print(err)
        
    finally:
        f.write( "\n" )
        sys.stdout.write( "\n" )


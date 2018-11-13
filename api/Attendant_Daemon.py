################################################################################
# This is the Daemon that keeps the HugAPI online and running as well as
#   hosting the functions used to interact with the database
#
# File:
#   /IRIS/api/Attendant_Daemon.py
################################################################################

# Third Party Imports
import sys
import os
import subprocess
import requests
import json

# Local Imports


# Self-defined global variables


# Variables to be assigned by config.yaml


# Check to make sure the api is still responding to requests and return 'online'
#   or 'offline' depending on the results
def checkAPIStatus():
    print("Checking status of the IRIS API")
    try:
        response = requests.get("http://localhost:8000/test_status").json()
    except:
        print("ERROR: API Not Responding")
        return 'offline'
    return response['status']


# Start the Attendant api
#   MAYBE use this... might just be better to use a cronjob and a shell script
#   though... decisions decisions....
def startAttendant():
    print("Starting up the Attendant api")
    if os.name == 'nt':
        subprocess.call("start Scripts\startAttendant.cmd", shell=True)
    # Need to test this...
    elif os.name =='posix':
        subprocess.call("hug -f Attendant.py &", shell=True)
    else:
        print("ERROR! UNSUPPORTED OPERATING SYSTEM DETECTED!")


################################################################################
# MAIN
################################################################################
def main(argv):
    print("\n==== API_Daemon.py ====\n")
    startAttendant()
    print(checkAPIStatus())
    quit()


if __name__ == "__main__":
    main(sys.argv[1:])

################################################################################
# File that listens for commands and changes from the server and instructs
#   the other pieces of the program to start, stop, change, etc.
#
# File:
#   /IRIS/Client/Client-Master.py
#
# Feature:
#   Agent
################################################################################

# Third Party Imports
import sys
import yaml
import datetime
import json
import requests

# Local Imports
import Runner
import Creator
import Minion_Container

# Self-defined global variables
isRunning = True
config = ''

# Variables to be assigned by config.yaml
IRIS_API_SERVER = ''
IRIS_APP_SERVER = ''
RUNNER_POLLING_RATE = ''
RUNNER_THREAD_COUNT = ''
RUNNER_FILE_COUNT = ''


# Send output to the log file
def log(logMessage):
    file = open("Logs/IRIS_Client.log", "a")
    file.write(logMessage)


# Update the global variables from config.yaml.
def readConfig():
    global config
    print("Reading config.yaml")
    with open("config.yaml", "r") as stream:
        try:
            config = yaml.load(stream)
        except yaml.YAMLError as yamlException:
            print("")
            print("Client-Master.py:readConfig() -- ", datetime.datetime.now())
            print(yamlException)

    global IRIS_API_SERVER
    IRIS_API_SERVER = config["Master"]["IRIS_API_SERVER"]
    global IRIS_APP_SERVER
    IRIS_APP_SERVER = config["Master"]["IRIS_APP_SERVER"]
    global RUNNER_POLLING_RATE
    RUNNER_POLLING_RATE = config["Master"]["RUNNER_POLLING_RATE"]
    global RUNNER_THREAD_COUNT
    RUNNER_THREAD_COUNT = config["Master"]["RUNNER_THREAD_COUNT"]
    global RUNNER_FILE_COUNT
    RUNNER_FILE_COUNT = config["Master"]["RUNNER_FILE_COUNT"]


# Poll the API to see if there are any new requests from the server
def checkServerRequests():
    global requestData
    print("Checking for change requests from: ", IRIS_API_SERVER)

    # Sample data before the api starts feeding the client
    requestData = {}
    requestData['job'] = "creator"
    requestData['job_id'] = 1
    requestData['pylon_source'] = "C:/Users/markw/Git_Repos/IRIS/Client/Default_Pylons/DefaultPylon.pdf"
    requestData['pylon_path'] = "C:/Users/markw/Desktop/pylon.pdf"
    requestData['hash_algorithm'] = "MD5"
    return requestData


# Check the config the server would like the minion to have, if any of the
#   Master options have changed update the local config and restart the
#   service/daemon so that the new values can be applied
def verifyConfig():
    print("Verifying config file(s) with application server:", IRIS_APP_SERVER)
    payload = {'hostname': 'BETTY'}
    response = requests.post("http://localhost:8000/request_config", data=payload)
    print(response.text)


# send job data and results back to the api
def informIRIS():
    payload = {'job_id': '00000004', 'run_result': 'SUCCESS', 'return_data': 'de189187bf1bacf3b4c73b2c6a04734b'}
    response = requests.post("http://localhost:8000/inform_iris", data=payload)
    print(response.text)


# Main function - starts up the functions to get IRIS running on the client
def main(argv):
    global isRunning
    print("Starting up Client-Master")
    readConfig()

    print("Running through api calls...")
    verifyConfig()
    informIRIS()

    # declare minion thread(s)
    myMinion = Minion_Container.Minion(1)

    while isRunning:
        verifyConfig()
        requestData = checkServerRequests()
        myMinion.giveData(requestData)
        myMinion.start()
        quit()


if __name__ == "__main__":
    main(sys.argv[1:])

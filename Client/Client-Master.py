################################################################################
# File that listens for commands and changes from the server and instructs
#   the other pieces of the program to start, stop, change, etc.
################################################################################

# Third Party Module Imports
import sys
import yaml
import datetime
import json

# Local Module Imports
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


# Update the global variables from config.yaml
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


# Poll the API to see if any pre-built commands are awaiting execution by the
#   IRIS Agent. These requests are NOT the directories for Runner to check
def checkServerRequests():
    global requestData
    print("Checking for change requests from: ", IRIS_API_SERVER)

    # Sample data before the api starts feeding the client
    requestData = {}
    requestData['job'] = "creator"
    requestData['job_id'] = 1
    requestData['pylon_source'] = "C:/Users/markw/Git_Repos/IRIS/Client/Default_\
        Pylons/DefaultPylon.pdf"
    requestData['pylon_path'] = "C:/Users/markw/Desktop/pylon.pdf"
    requestData['hash_algorithm'] = "MD5"
    return requestData


# Check the config the server would like the minion to have, if any of the
#   Master options have changed update the local config and restart the
#   service/daemon so that the new values can be applied
def verifyConfig():
    print("Verifying config file(s) with application server:", IRIS_APP_SERVER)


# DEBUG: pauses services and waits for user input
def debug_awaitInteraction():
    input("Hit 'Enter' to proceed...")


# DEBUG: displays the values of the config variables
def debug_displayConfig():
    print("")
    print("\n==== Displaying config data in different forms ====\n")
    print("")
    print("Displaying config variables...")
    print("IRIS_API_SERVER          ", IRIS_API_SERVER)
    print("IRIS_APP_SERVER          ", IRIS_APP_SERVER)
    print("RUNNER_POLLING_RATE      ", RUNNER_POLLING_RATE)
    print("RUNNER_THREAD_COUNT      ", RUNNER_THREAD_COUNT)
    print("RUNNER_FILE_COUNT   ", RUNNER_FILE_COUNT)
    print("")
    print("Displaying raw config data...")
    print(config)
    print("")
    print("Displaying raw data JSON Export data...")
    print(json.dumps(config))


# running processes designed to be multithreaded (not yet but will be)
def minion(threadNumber):
    isRunning = True
    print("Thread Number ", threadNumber, " started")

    # JSON variables
    MasterRequestData_JSON = ''
    MasterResponseData_JSON = ''
    ConfigData_JSON = ''

    while isRunning:
        print("Entering Loop")
        # API Communication
        MasterRequestData_JSON = checkServerRequests()
        ConfigData_JSON = verifyConfig()

        print(MasterRequestData_JSON)

        # Either start up the runner or the creator depending on the input
        #   received by the latest api call
        # grabRunnerJobs()
        # buildPylon()

        isRunning = False


# Main function - starts up the functions to get IRIS running on the client
def main(argv):
    global isRunning
    print("Starting up Client-Master")
    readConfig()

    myMinion = Minion_Container.Minion(1)
    # print(checkServerRequests())
    requestData = checkServerRequests()
    myMinion.giveData(requestData)
    myMinion.start()


if __name__ == "__main__":
    main(sys.argv[1:])

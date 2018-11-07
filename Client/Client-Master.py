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

# Self-defined global variables
isRunning = True
config = ''

# Variables to be assigned by config.yaml
IRIS_API_SERVER = ''
IRIS_APP_SERVER = ''
RUNNER_POLLING_RATE = ''
RUNNER_THREAD_COUNT = ''
RUNNER_FILE_COUNT = ''

# Grab the contents of config.yaml and update the global variables with this data
def readConfig():
    global config
    print("Reading config.yaml")
    with open("config.yaml", "r") as stream:
        try:
            config=yaml.load(stream)
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


# Poll the API to see if any pre-built commands are awaiting execution by the IRIS Agent.
#   These requests are NOT the directories for Runner to check
def checkServerRequests():
    print("Checking for change requests from: ", IRIS_API_SERVER)
    # TODO: Think of a good way to do this without making direct calls to system, don't make an option of this that allows for actual commands to be sent unless the user absolutely wants that and they can choose it with ALLOW_REMOTE_COMMANDS


# Check the config the server would like the minion to have, if the config is
#   any different, change it and restart the service/daemon
def verifyConfig():
    print("Verifying config file(s) with application server:", IRIS_APP_SERVER)


# Grab the JSON from the server for <RUNNER_FILE_COUNT> different file locations.
def grabRunnerJobs():
    print("")
    print("Sending Jobs to the runner...")

    # Simply a test sample until the server code is.... started....
    # {"0": "C:\Temp\DocumentA.rtf", "1": "C:\Temp\DocumentB.docx", "2": "C:\Temp\DocumentC.pdf", "3": "C:\Temp\DocumentD.txt"}
    runnerJobs_JSON = {}
    runnerJobs_JSON['numJobs'] = 4 # if this somehow goes bad things PROBABLY won't go well, add in error allowance in api/server if one is missing or extra or just find a better way to do it
    runnerJobs_JSON['0'] = "C:\Temp\DocumentA.rtf"
    runnerJobs_JSON['1'] = "C:\Temp\DocumentB.docx"
    runnerJobs_JSON['2'] = "C:\Temp\DocumentC.pdf"
    runnerJobs_JSON['3'] = "C:\Temp\DocumentD.txt"
    runnerJobs_JSON['checksum'] = "MD5"
    Runner.runJobs(runnerJobs_JSON)


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


# DEBUG: Set the primary loop conditional to be false so that it will stop
#   Running after the current iteration
def debug_stopMaster():
    global isRunning
    isRunning = False


# Main function
def main(argv):
    global isRunning
    print("Starting up Client-Master")
    readConfig()

    serverRequests_JSON = ''
    configVerification_JSON = ''

    while isRunning:
        # API Communication
        serverRequests_JSON = checkServerRequests()
        configVerification_JSON = verifyConfig()
        grabRunnerJobs()

        print("JSON From Server Request: ", serverRequests_JSON)
        print("JSON From Config Verification Request ", configVerification_JSON)

        # Debugging calls
        # debug_displayConfig()
        debug_stopMaster()


if __name__ == "__main__":
    main(sys.argv[1:])

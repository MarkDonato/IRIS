################################################################################
# Python file that will hold the Minion Class, which is responsible for actually
#   running the jobs requested by the Master.
#
# File:
#   /IRIS/Client/Minion-Container.py
#
# Module:
#   Agent
################################################################################

# Third Party Module Imports
import json

# Local Module Imports
import Creator
import Runner

# Self-defined global variables
dataBuffer = ''
id = ''

class Minion:

    def __init__(self, minionNumber):
        self.id = minionNumber

    # Accessor method for calling program to feed this minion json data for it
    #   to work with
    def giveData(self, MasterRequestData):
        global dataHolder
        print("giving data to Minion")
        self.dataBuffer = MasterRequestData


    # Build a pylon given a particular source and target
    def buildPylon(filePath, sourceFile, checksum):
        return Creator.buildPylon(filePath, sourceFile, checksum)


    # Grab the JSON from the server for <RUNNER_FILE_COUNT> different file locations
    def grabRunnerJobs():
        print("")
        print("Sending Jobs to the runner...")

        # Sample data before the api starts feeding the client
        runnerJobs_JSON = {}
        runnerJobs_JSON['numJobs'] = 4
        runnerJobs_JSON['0'] = "C:\Temp\DocumentA.rtf"
        runnerJobs_JSON['1'] = "C:\Temp\DocumentB.docx"
        runnerJobs_JSON['2'] = "C:\Temp\DocumentC.pdf"
        runnerJobs_JSON['3'] = "C:\Temp\DocumentD.txt"
        runnerJobs_JSON['checksum'] = "MD5"
        Runner.runJobs(runnerJobs_JSON)


    # do stuff
    def start(self):
        print("Minion", self.id, "has started...")
        
        if self.dataBuffer['job'] == "creator":
            print("Calling creator")
            Creator.buildPylon(self.dataBuffer['pylon_path'], self.dataBuffer['pylon_source'], self.dataBuffer['hash_algorithm'])
        elif self.dataBuffer['job'] == 'runner':
            print("Calling runner")

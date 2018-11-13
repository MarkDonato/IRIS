################################################################################
# Python Hug API for IRIS
#
# File:
#   /IRIS/api/Attendant.py
################################################################################

# Third Party Imports
import sys
import random
import hug
import yaml

# Local Imports
import Attendant_Daemon

# Self-defined global variables


# Variables to be assigned by config.yaml


# The api method that returns the job to perform next. Currently using RNG to
#   try out different options that are unexpected but this will be changed when
#   the rest of the IRIS stack is functional and talking to each other.
# Warning: This is a GET which we definitely don't want to use for any calls
#   unless absolutely necessary or by the user's choice for whatever reason
#   TODO: make config setting to allow option to change this.
@hug.cli()
@hug.get(examples='hostname=MY-JOB-REQUESTER')
def request_job_get(hostname: hug.types.text, hug_timer=3):
    decision = random.randint(1, 3)

    if decision == 1:
        return {'job_type': 'creator',
                'job_id': '00000001',
                'pylon_source': 'C:/Users/markw/Git_Repos/IRIS/Client/Default_Pylons/DefaultPylon.pdf',
                'target_directory': 'C:/Users/markw/Desktop/pylon.pdf',
                'hash_algorithm': 'MD5',
                'response_time': float(hug_timer)}
    elif decision == 2:
        return {'job_type': 'runner',
                'job_id': '00000002',
                'pylon_path': 'C:/Users/markw/Desktop/pylon.pdf',
                'hash_algorithm': 'MD5',
                'response_time': float(hug_timer)}
    elif decision == 3:
        return {'job_type': 'none',
                'response_time': float(hug_timer)}


# The api method that returns the job to perform next. Currently using RNG to
#   try out different options that are unexpected but this will be changed when
#   the rest of the IRIS stack is functional and talking to each other.
@hug.cli()
@hug.post()
def request_job(hostname: hug.types.text, hug_timer=3):
    decision = random.randint(1, 3)

    if decision == 1:
        return {'job_type': 'creator',
                'job_id': '00000001',
                'pylon_source': 'C:/Users/markw/Git_Repos/IRIS/Client/Default_Pylons/DefaultPylon.pdf',
                'target_directory': 'C:/Users/markw/Desktop/pylon.pdf',
                'hash_algorithm': 'MD5',
                'response_time': float(hug_timer)}
    elif decision == 2:
        return {'job_type': 'runner',
                'job_id': '00000002',
                'pylon_path': 'C:/Users/markw/Desktop/pylon.pdf',
                'hash_algorithm': 'MD5',
                'response_time': float(hug_timer)}
    elif decision == 3:
        return {'job_type': 'none',
                'response_time': float(hug_timer)}


# The api method that returns the config a client is supposed to be using.
#   Currently using a base config.yaml file but later on this data should be
#   stored and pulled from the IRIS database
# Warning: This is a GET which we definitely don't want to use for any calls
#   unless absolutely necessary or by the user's choice for whatever reason
#   TODO: make config setting to allow option to change this.
@hug.cli()
@hug.get(examples='hostname=MY-CONFIG-REQUESTER')
def request_config_get(hostname: hug.types.text, hug_timer=3):
    # For now return a copy of config.yaml. Later pull from SQL for hostname
    print("Reading config.yaml")
    with open("config.yaml", "r") as stream:
        try:
            config = yaml.load(stream)
        except yaml.YAMLError as yamlException:
            print("")
            print("Client-Master.py:readConfig() -- ", datetime.datetime.now())
            print(yamlException)

    return config


# The api method that returns the config a client is supposed to be using.
#   Currently using a base config.yaml file but later on this data should be
#   stored and pulled from the IRIS database
@hug.cli()
@hug.post()
def request_config(hostname: hug.types.text, hug_timer=3):
    # For now return a copy of config.yaml. Later pull from SQL for hostname
    print("Reading config.yaml")
    with open("config.yaml", "r") as stream:
        try:
            config = yaml.load(stream)
        except yaml.YAMLError as yamlException:
            print("")
            print("Client-Master.py:readConfig() -- ", datetime.datetime.now())
            print(yamlException)

    return config


# The api method that sends the job status and results messages to the api. This
#   will still need to be integrated into actual database changes
# Warning: This is a GET which we definitely don't want to use for any calls
#   unless absolutely necessary or by the user's choice for whatever reason
#   TODO: make config setting to allow option to change this.
@hug.cli()
@hug.get(examples='job_id=00000004&run_result=SUCCESS&return_data=de189187bf1bacf3b4c73b2c6a04734b')
def inform_iris_get(job_id: hug.types.text,
                run_result: hug.types.text,
                return_data: hug.types.text,
                hug_timer=3):
    print("Informing IRIS")


# The api method that sends the job status and results messages to the api. This
#   will still need to be integrated into actual database changes
@hug.cli()
@hug.post()
def inform_iris(job_id: hug.types.text,
                run_result: hug.types.text,
                return_data: hug.types.text,
                hug_timer=3):
    print("Informing IRIS")
    print(job_id)
    print(run_result)
    print(return_data)

    return {'result': 'success'}


# This api method is simply to test to make sure the attendant is up and running
@hug.get(examples='')
def test_status():
    return{'status': 'online'}


################################################################################
# MAIN
################################################################################
def main(argv):
    print("\n==== Attendant.py ====\n")
    print("This file should never be called directly.")
    print("To use: utilize the 'hug' command after running 'pip install hug'\n")
    print("Quick Note/TODO(from hug.rest/website/quickstart):")
    print("\tSee hug.rest/website/quickstart for use in a production system.")

    quit()


if __name__ == "__main__":
    main(sys.argv[1:])


################################################################################
# TODO/NOTES:
#
# BIG: Change all these crappy GET requests into POST requests.
#
# Setup Authentication and tokens and all those goodies.
#
# Setup SQL structure and decide which type of database I want to use.
#   Currently between MySQL, PostgreSQL, and MongoDB
#   If the SQL server is not the same as the api server maybe use sqlite3 to
#       decrease the latency of requests. (Throw recently used items into a
#       sqlite3 cache, of sorts)
################################################################################

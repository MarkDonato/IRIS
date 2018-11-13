################################################################################
# Python Hug API for IRIS
#
# File:
#   /IRIS/api/HugAPI.py
################################################################################

# Third Party Imports
import sys
import random
import hug

# Local Imports
import API_Daemon

# Self-defined global variables


# Variables to be assigned by config.yaml


# The api method that returns a job to perform next. Currently using RNG to
#   try out different options that are unexpected but this will be changed when
#   the rest of the IRIS stack is functional and talking to each other.
@hug.cli() # hug -f HugAPI.py -c MYPC
# provides an example on the format of an api call for request_job
@hug.get(examples='hostname=MYPC') # hug -f HugAPI.py
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


################################################################################
# MAIN
################################################################################
def main(argv):
    print("\n==== HugAPI.py ====\n")
    print("This file should never be called directly.")
    print("To use: utilize the 'hug' command after running 'pip install hug'\n")
    print("\tQuick Note/TODO(from hug.rest/website/quickstart)")
    print("It's important to note that it's generally never a good idea to use\
    a development server (like hug's, Flask's, etc.) directly in production.\
    Instead, a WSGI-compatible server (such as uwsgi or Gunicorn) is\
    recommended. Every hug API that contains an http endpoint automatically\
    exposes a `__hug_wsgi__` WSGI-compatible API - making integration of our\
    above example a breeze:\n")
    print("Examples:")
    print("Using uwsgi")
    print("'uwsgi --http 0.0.0.0:8000 --wsgi-file first_step_3.py --callable\
    __hug_wsgi__'\n")
    print("Using gunicorn")
    print("'gunicorn first_step_3:__hug_wsgi__'\n")

    quit()


if __name__ == "__main__":
    main(sys.argv[1:])

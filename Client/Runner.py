################################################################################
# File/process responsible for Running around to check and create the files the
#   master requests.
################################################################################

# Import Modules
import sys
import hashlib

# Global Variables
# runner_id = ''
jobData = ''


# Hash out the specified file with the given hash algorithm in jobData
def hashFile(filePath):
    # filePath has white space on either side, need to sed that outta there
    print("Hashing", filePath, "with", jobData['checksum'], "hashing algorithm")
    if jobData['checksum'] == "MD5":
        # This could probably use a re-write
        print(hashlib.md5(open(filePath, 'rb').read()).hexdigest())
    elif jobData['checksum'] == "SHA1":
        print("NA")
    elif jobData['checksum'] == "SHA224":
        print("NA")
    elif jobData['checksum'] == "SHA256":
        print("NA")
    elif jobData['checksum'] == "SHA384":
        print("NA")
    elif jobData['checksum'] == "SHA512":
        print("NA")
    else:
        print("Unsupported Hash algorithm requested: ", jobData['checksum'])


# set and keep track of the runner ID
def setID(id):
    global runner_id
    runner_id = id


# take in the JSON object from the master
def runJobs(jobRequests_JSON):
    print("\n==== Jobs received at runner ====\n")
    global jobData
    jobData = jobRequests_JSON

    # Iterate through each requested file
    for i in range(0, jobData['numJobs']):
        hashFile(jobData[str(i)])
    print("")


# Runner Main exists to instruct user to either use Client-Master.py to call
#   runner or use the available command line options to run a single threaded
#   version of runner, on a particular target for testing purposes
def main(argv):
    print("\n==== Runner.py ====\n")
    print("TODO: Make this do/say something")
    sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])
# Self-defined global variables

################################################################################
# File/process responsible for creating new files and sending the data for those
#   files to the master so that it may send this data to the server
################################################################################

# Import Modules
import sys
import yaml
import datetime
import shutil
import hashlib

# Local Imports

# Self-defined global variables
config = ''

# Variables to be assigned by config.yaml
HASH_ALGORITHM = ''


# Update the global variables from config.yaml
def readConfig():
    global config
    print("Reading config.yaml")
    with open("config.yaml", "r") as stream:
        try:
            config = yaml.load(stream)
        except yaml.YAMLError as yamlException:
            print("")
            print("Creator.py:readConfig() -- ", datetime.datetime.now())
            print(yamlException)

    global HASH_ALGORITHM
    HASH_ALGORITHM = config["Creator"]["HASH_ALGORITHM"]


# Given a file path and a checksum algorithm to use, hash out the file
#   and return the checksum value
def hashFile(filePath, hashAlgorithm):
    print("Hashing", filePath, " with ", hashAlgorithm, "hashing algorithm")
    pylonCheckSum = ''
    if hashAlgorithm == "MD5":
        # This could probably use a re-write
        print(hashlib.md5(open(filePath, 'rb').read()).hexdigest())
        pylonCheckSum = hashlib.md5(open(filePath, 'rb').read()).hexdigest()
    elif hashAlgorithm == "SHA1":
        print("SHA1 CURRENTLY UNAVAILABLE IN CREATOR.HASHFILE()")
    elif hashAlgorithm == "SHA224":
        print("SHA224 CURRENTLY UNAVAILABLE IN CREATOR.HASHFILE()")
    elif hashAlgorithm == "SHA256":
        print("SH256 CURRENTLY UNAVAILABLE IN CREATOR.HASHFILE()")
    elif hashAlgorithm == "SHA384":
        print("SHA384 CURRENTLY UNAVAILABLE IN CREATOR.HASHFILE()")
    elif hashAlgorithm == "SHA512":
        print("SHA512 CURRENTLY UNAVAILABLE IN CREATOR.HASHFILE()")
    else:
        print("Unsupported Hash algorithm requested: ", hashAlgorithm)

    return pylonCheckSum


# Given a file to use and a path to place it, creates a new pylon. Returns the
#   checksum of the file.
def buildPylon(filePath, sourceFile, checksumAlgorithm):
    pylonCheckSum = ''
    print("Constructing Pylon at ", filePath)
    shutil.copy(sourceFile, filePath)
    pylonCheckSum = hashFile(filePath, checksumAlgorithm)
    print("The checksum of the pylon is ", pylonCheckSum)
    return pylonCheckSum


# Creator Main exists to instruct user to use Client-Master.py to call
#   creator. This will also display some quick information about the Creator and
#   what it does with some examples and other nifty little tips
def main(argv):
    print("\n==== Creator.py ====\n")

    print("\n'Creator.py' is reponsible for the creation of pylons as well as \n\
    grabbing the initial checksums of those pylons based on the checksum \n\
    protocol specified in 'config.yaml'")

    print("\nUSAGE: Creator.py functionality is invoked by 'Client-Master.py' \n\
    and is not intended to run as a standalone file. View the help page of \n\
    'Client-Master.py' to see how to create and checksum single files manually")

    print("")

    displayChecksum = buildPylon(
        "C:/Users/markw/Desktop/testDocument.docx",
        "C:/Users/markw/Git_Repos/IRIS/Client/Default_Pylons/DefaultPylon.docx",
        "MD5")
    print(displayChecksum)

    sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])

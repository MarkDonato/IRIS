################################################################################
# File/process responsible for creating new files and sending the data for those
#   files to the master so that it may send this data to the server
################################################################################

# Import Modules
import sys
import yaml

# Self-defined global variables
config = ''

# Variables to be assigned by config.yaml
HASH_ALGORITHM = ''

# Grab the contents of config.yaml and update the global variables with this data
def readConfig():
    global config
    print("Reading config.yaml")
    with open("config.yaml", "r") as stream:
        try:
            config=yaml.load(stream)
        except yaml.YAMLError as yamlException:
            print("")
            print("Creator.py:readConfig() -- ", datetime.datetime.now())
            print(yamlException)

    global HASH_ALGORITHM
    HASH_ALGORITHM = config["Creator"]["HASH_ALGORITHM"]

# Hash out the specified file with the algorithm defined in config.yaml
def hashFile(filePath, algorithm):
    readConfig()
    print(HASH_ALGORITHM)



# Creator Main exists to instruct user to use Client-Master.py to call
#   creator. This will also display some quick information about the Creator and
#   what it does with some examples and other nifty little tips
def main(argv):
    print("\n==== Creator.py ====\n")

    print("\n'Creator.py' is reponsible for the creation of pylons as well as \n\
    grabbing the initial checksums of those pylons based on the checksum \n\
    protocol specified in 'config.yaml'.")

    print("\nUSAGE: Creator.py functionality is invoked by 'Client-Master.py' \n\
    and is not intended to run as a standalone file. View the help page of \n\
    'Client-Master.py' to see how to create and checksum single files manually.")

    sys.exit()

if __name__ == "__main__":
    main(sys.argv[1:])

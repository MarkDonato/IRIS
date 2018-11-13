################################################################################
# Given paramters supplied from a yaml file, send a basic alert email
#
# File:
#   /IRIS/Srv/Alerting/Email_Client.py
#
# Feature:
#   Alerting
################################################################################

# Third Party Imports
import sys
import yaml
import smtplib
import getopt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

# Local Imports

################################################################################
# MAIN
################################################################################
def main(argv):
    # Inject config.yaml into 'data'
    with open("emailConfig.yaml", "r") as stream:
        try:
            data = yaml.load(stream)
            data['smtpserver']
        except yaml.YAMLError as yamlException:
            print(yamlException)

    # Define variables based on emailConfig.yaml
    SMTP_SERVER = data['smtpserver']
    SMTP_PORT = data['smtpport']
    SENDER = data['sender']
    PASSWORD = data['password']
    RECIPIENT = data['recipient']
    SUBJECT = data['subject']
    MESSAGE = data['message']

    # Adjust settings based on command line arguments thrown
    print("")
    print("Parsing command line options...")
    try:
        opts, args = getopt.getopt(
            argv,
            "dhm:r:s:",
            ["message_storage=", "recipient_storage=", "subject_storage="])
    except getopt.GetoptError:
        print("NO PARAMETERS SUPPLIED. USE -h TO VIEW OPTIONS. EXITING...")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("")
            print("IRIS server email client")
            print(" USAGE:")
            print("  Single Options:")
            print("     python emailClient.py -h")
            print("      -->  Display this help message")
            print("     python emailClient.py -d")
            print("      -->  Use the defaults configured in config.yaml")
            print("  Multiple Options:")
            print("     python emailClient.py -m  <my_message>")
            print("      -->  Specify the message you would like to send")
            print("     python emailClient.py -r  <my_recipient>")
            print("      -->  Specify the recipient you would like to send to")
            sys.exit()
        if opt == '-d':
            print("Using defaults specified in ./config.yaml")
        else:
            if opt in ("-m", "--message"):
                print("Using supplied message: ", arg)
                MESSAGE = arg
            if opt in ("-r", "--recipient"):
                print("Using supplied recipient: ", arg)
                RECIPIENT = arg
            if opt in ("-s", "--subject"):
                print("Using supplied subject: ", arg)
                SUBJECT = arg

    # Display the acquired config settings
    print("")
    print("SMTP Server: ", SMTP_SERVER)
    print("SMTP_PORT: ", SMTP_PORT)
    print("SENDER: ", SENDER)
    print("PASSWORD: ", PASSWORD)
    print("RECIPIENT: ", RECIPIENT)
    print("SUBJECT: ", SUBJECT)
    print("MESSAGE: ", MESSAGE)

    # Concatenate brand thank you on end of alert message
    MESSAGE += "\n\n\n\nThank you for using IRIS.\n\nhttps://IRISWebsite.tech"

    # Email content setup
    print("Building Email...")
    msg = MIMEMultipart()
    msg["Subject"] = SUBJECT
    msg["To"] = RECIPIENT
    msg["From"] = SENDER
    content = MIMEText('text', "plain")
    content.set_payload(MESSAGE)
    msg.attach(content)

    # Network Communication
    print("Instantiating network communication and pre-requisites...")
    try:
        connection = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        connection.ehlo()
    except Exception:
        print("Error sending ehlo to Email Provider!")
    connection.starttls()
    connection.ehlo()
    connection.login(SENDER, PASSWORD)

    # Encode the email
    print("Sending Email...")
    encoders.encode_base64
    finalMessage = msg.as_string()

    # Send out the alert
    connection.sendmail(SENDER, RECIPIENT, finalMessage)
    connection.quit()


if __name__ == "__main__":
    main(sys.argv[1:])

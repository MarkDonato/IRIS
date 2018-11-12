# Information Relay Integrity System [I.R.I.S.]

## Development
**Mark Donato**
* markwd122594@gmail.com
* https://github.com/MarkDonato

## What is it and why should I care?
IRIS is meant to be a primarily python-based all-in-one security suite designed for combining many security and monitoring functions into one. I see IRIS as being more than just an IDS system though. Not only will IRIS monitor what is happening in the servers reporting to it; it will also analyze this data, recommend configuration changes it sees as worrisome, enact automated emergency measures(alerts, server lockdowns, file security changes, etc.) and more. IRIS is not a replacement for in-place tools today but rather a complement to those tools. IRIS is planned to have many internal functions in it and I would also like for it to integrate pretty seamlessly with already popular systems such as Graylog, Splunk, LibreNMS, Nmap, SaltStack and more.

## Components

### Client
Planned Supported Platforms: Windows, Linux variations, OSX, Unix variations

Planned Purpose: The client is an agent installed locally on all systems that will interact with IRIS in any way (including the IRIS Server(s))

### API
Planned Supported Platforms: Linux, Windows (maybe)

Planned Purpose: The API is a python hug application that handles transferring of JSON data between the application server and clients as well as temporary data storage and cache for commonly used/expected data. The API may be installed on the application server or on its own depending on how many Clients are connecting to the IRIS instance.

### Application Server
Planned Supported Platforms: Linux

The application server processes the data fed to it as well as hosts the IRIS web service.

### Other
A mobile app might be cool one day...

## Modules

### Agent
The agent is the heart and brains of the IRIS client. It keeps the modules running, calls them when they need to be ran, manages job scheduling and performs maintenance on anything that is off.

### Pylon Real-Time historical comparison monitor (come up with a better name)
By using randomly scattered files called "Pylons" and getting the checksum of those Pylons to send back to the monitor server, if an automated ransomware attack is running rampant and hits one of the Pylons the server will be alerted. From there sys admins have the option to set reaction settings on a per-node basis. Reactions may include changing permissions to stop non-admin users from changing files, sending out an email to desired addresses, making API calls to non-IRIS infrastructure (i.e. automated SMS system, a logging server, etc.), Injecting a custom script, etc.

### Nurse
Nurse is designed to be a quick and easy way to view how hard systems are running as well as show other usage stats and display them in an easily legible way so that data can be grouped up together in graphs on a page. Lots of people have already done it, but this is just meant to be a convenience that is built in to the IRIS Suite.

### Windows Firewall Evaluation [WFE]
WFE will be a small module that sends back the firewall settings of a workstation/server through the stack to be analyzed by the IRIS Application Server. From there it will easily list out the primary settings and rules as well as list all ports that are open to inbound traffic.

## When
Currently this is just being built in free time outside of my personal occupation, so I do not have any set deadlines.

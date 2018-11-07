# Information Relay Integrity Software [I.R.I.S.]

## Who
 Mark Donato
 markwd122594@gmail.com
 https://github.com/MarkDonato

## What
Information Relay Integrity Software or IRIS for short is a real time client-server infrastructure monitoring and
  reaction tool designed to fight against Ransomware attacks.

## Why
Not every company can afford a fully developed security team. Not every Administrator wants to set up their own automation or deal with any programming at all really. So, IRIS is here to provide a small lending hand to those SysAdmins. For the more advanced users the project is Open Source. Modify it, break it, make it better (if you have a better way to accomplish a task here, let me know! I am not a prideful person, a better way to do something is the better way!).

## How
By using randomly scattered files called "Pylons" and getting the checksum of those Pylons to send back to the monitor server, if an automated ransomware attack is running rampant and hits one of the Pylons the server is alerted. From there the Administrators have a choice to set before hand on each Node about how to react. Reactions may include running something like cacls to change permissions and stop non-admin users from changing files, sending out an email to desired addresses, making an API call to something the administrator sets up (i.e. automated SMS system, a logging server, etc.), or more!(to come)

## When
Currently this is just being built in free time outside of my personal occupation, so I do not have any set deadlines.

## Potential Ideas
See about getting logging on the Pylons so that they may see what process/user/whatever may have changed them

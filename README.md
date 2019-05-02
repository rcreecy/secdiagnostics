## Security Diagnostics Utility
#### The purpose of this tool is to identify possible errors with the compatible AV software in one click

![GUI Screenshot](https://raw.githubusercontent.com/rcreecy/secdiagnostics/master/images/screenshot.PNG "GUI Screenshot")

#### Current Functionality
* Does a check of the service running (McAfee McShield)
* Outputs the HostName and Computer Name (mostly for utilizing these variables later)
* Current CPU usage total on system (** WIP: for any CPU usage over threshhold, also output violating PID/name **)
* Plants an EICAR test file on the computers desktop path, waits 10 seconds, and checks again for the presence of the file to assess real time scanning 
  * EICAR testing can be disabled/enabled through the options menu, to prevent noisy threat events occuring
* Log Parsing - Still WIP, however, but the core premise of being able to output lines from logs containing certain phrases should be relatively easy. Will be getting more complex as time goes on



___
#### Work in Progress
* Streamline rule creation by placing rules in seperate module and loop through them, outputting returns until end is reached
* Rule to search for "value 3" in MSI installer logs, and output preceeding 10 lines and 5 post lines into console to identify any installation issues
* Rule to validate any network open listening ports
* Come up with new rules??
* Log Parsing based on known issue information


___
Built on Python 3.7.2
To build, simply clone the repo and run the main.py script. Requires a few dependencies.

This is being built mostly to expand my python knowledge and skills. This project will revolve around the software suite I am familiar with, and eventually possibly expand into more umbrella like interaction with AV solutions, as I advance my skills. I would in no way consider this a real tool at this time.
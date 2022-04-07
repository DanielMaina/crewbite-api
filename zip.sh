#!/bin/bash

# Invoke with "./zip.sh" in a bash shell.
# This is not a part of the production code! This is just a tool to packing up files for uploading to AWS Elastic Beanstalk.
rm crewbite.zip
if [[ "$OSTYPE" == "cygwin" || "$OSTYPE" == "msys" ]]; then
    # For Windows, 7zip has to be installed on windows and the path that 7z.exe lives needs to be in the $PATH environment variable.
    7z a -tzip crewbite.zip crewbite application.py .ebextensions requirements.txt
else
    # For Max OS X and Linux
    zip crewbite.zip -r crewbite application.py .ebextensions requirements.txt
fi
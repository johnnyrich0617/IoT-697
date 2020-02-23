#!/bin/bash

# What OS are we running on?
# right now this script will only apply to linux-gnu
sitePackagesLoc = 'unknown'
if [[ "$OSTYPE" == "linux-gnu" ]]; then
    sitePackagesLoc = ~/.local/lib/python27/site-packages
else
  echo Must be running on Linux OS to run this script
  echo Exiting.......................
  exit
fi

if [ ! -d "$sitePackagesLoc" ]; then
    
else


fi


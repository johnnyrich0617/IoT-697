#!/bin/bash

echo "This script will install the required python packages needed to execute"
echo "the HomeWeatherReporter application."
echo
echo "Would you like to continue?"
read -p '[ y ] or [ n ]: ' answer

if [[! $answer == "y" && ! $answer == "n"]] then
    echo Not an expected response, exiting......
    exit
elif [$answer == "n"] then
    exit
else 
    echo "-----------Installing Python Packages------------"
    echo "-------------------------------------------------"
    echo "-------------------------------------------------"
    # What OS are we running on?
    # right now this script will only apply to linux-gnu
    # we are targeting a pi raspian (debian) flavor
    sitePackagesLoc = 'unknown'
    if [[ "$OSTYPE" == "linux-gnu" ]]; then
        sitePackagesLoc = $HOME/.local/lib/python27/site-packages
    else
      echo "Must be running on Linux OS to run this script"
      echo "Exiting......................."
      exit
    fi
    # check to see if the python27 sitepackages directory exits
    # so that we can load the project python packages into it correctly
    # for runtime
    if [ ! -d "$sitePackagesLoc" ]; then
        echo
        echo "The Python Package Repository location $sitePackagesLoc does not exist...."
        echo "Creating python27 site-packages repository.................."
        echo
        # the -p option will create the entire path if it does not exist
        mkdir -p $sitePackagesLoc  
    fi
    echo
    echo "Copying HomeWeatherReporter packages to repository........"
    echo "................."
    cp -a ../messages $sitePackagesLoc
    cp -a ../utils $sitePackagesLoc
    cp -a ../pi_sensors $sitePackagesLoc
    echo
    echo "Completed copying required Python packages to Python27 Package Repository: $sitePackagesLoc"
fi




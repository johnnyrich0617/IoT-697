#!/bin/bash

echo ---------------------------------------------------------------------------
echo -------------Starting Home Weather Reporter--------------------------------
echo ---------------------------------------------------------------------------

# execute installing the python packages
# this will prompt the user to see if this needs to occur
source ./runtime_env.sh

#execute the python script
python ./HomeWeatherDisplayMQTT.py
echo ----------------------------------------------------------------------------
echo -------------Shutdown Home Weather Reporter Complete------------------------
echo ----------------------------------------------------------------------------

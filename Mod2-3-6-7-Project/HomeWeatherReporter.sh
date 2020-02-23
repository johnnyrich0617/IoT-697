#!/bin/bash
#Source the runtime env for the python script
#echo Sourcing runtime environment.......................
#source ./runtime_env.sh

echo ---------------------------------------------------------------------------
echo -------------Starting Home Weather Reporter..................... ----------
echo ---------------------------------------------------------------------------
#execute the python script
python ./HomeWeatherDisplayMQTT.py
echo ----------------------------------------------------------------------------
echo -------------Shutdown Home Weather Reporter Complete............ -----------
echo ----------------------------------------------------------------------------
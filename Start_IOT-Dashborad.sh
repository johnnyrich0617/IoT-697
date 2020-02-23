#!/bin/bash

echo --------------------------------------------------
echo --------------------------------------------------
echo -----------------IOT DASHBOARD -------------------
echo --------------------------------------------------
echo --------------------------------------------------
echo
echo
echo Starting IOT Dashboard............................
echo cd MOD-7-Client/iot ..............................
# Chnage dir to exec dir, or exit if Dir does not exist
cd MOD-7-Client/iot || exit
pwd
echo
echo
echo Running npm start............................
# You can set the connection string for any mongo instance here
# in the package.json file on the npm start line
# defualt for meteor is embedded mongo.
# start with npm to use selected Mongo running, (e.g in Docker or lan instance)
# in my case I am running mongo in a Docker container
npm start
echo Stopping IOT DASHBOARD........................
echo
echo
echo --------------------------------------------------
echo --------------------------------------------------
echo ---------SHUTDOWN IOT DASHBOARD COMPLETE----------
echo --------------------------------------------------
echo --------------------------------------------------
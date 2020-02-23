#!/bin/bash

echo --------------------------------------------------
echo --------------------------------------------------
echo -----------------SIMPLE TODOs---------------------
echo --------------------------------------------------
echo --------------------------------------------------
echo
echo
echo Starting Simple ToDos Tutorial....................
echo cd MOD-5-Project/Tutorials/simple-todos...........
# Chnage dir to exec dir
cd MOD-5-Project/Tutorials/simple-todos || exit
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
echo Stopping Simple ToDos........................
echo
echo
echo --------------------------------------------------
echo --------------------------------------------------
echo ---------SHUTDOWN SIMPLE TODOs COMPLETE-----------
echo --------------------------------------------------
echo --------------------------------------------------

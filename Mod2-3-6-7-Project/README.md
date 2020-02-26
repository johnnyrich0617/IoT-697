# Home Weather Reporter

### Requirments and Assumptions
* Running on Raspberry Pi with Raspian as the OS
* Requires Python 2.7, does not support Python 3.X as of lastest
* Assumes the use of GrovePi+ board

### Execution
* Execute the following chmod cmds:
  * chmod 700 runtime_env.sh
    * This script will setup the python repository and install specific python packages
  * chmod 700 HomeWeatherReporter.sh
    * This script is the main python application loop
* From within this directory, execute the HomeWeatherReporter.sh, "./HomeWeatherReporter.sh"
  * Upon execution you will be prompted to perform setup options, you will need to perform the options at least once
  * Execute the supplied python script

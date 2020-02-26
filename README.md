# IoT-697
## mqtt-test-code
Contains code for testing MQTT test code for localhost and test.mqtt.org connections

## Mod2-3-6-7Project
Contains the code for Python code used for pub/sub
* For Module 6 and 7:
  * read the README.md located in that directory
  * Follow the instructions in the readme.md to execute
  * The python package environement needs to be setup by the scripts.

## MOD4-LED-Project
Contains code for IOT 697 Module 4  LED - NodeRed - REST

## MOD5-Client
Contain Meteor Client code for Module 5 (ToDos Tutorial Code)

* To execute the client code perform the following;
  * In the root, open a terminal and type chmod 700 Start_ToDos_Client.sh ,  select enter
  * Now, type ./Start_ToDos_Client.sh
  * You should see Meteor start in the terminal
    ** This assumes you have Mongo running external from Meteor, this property is set in the package.json (top line, Start)
    ** If this is not your setup, Do not use this script, run meteor from inside the client dir by typing 'meteor"
  
## MOD7 Client
Contains the Meteor Client for Module 7

* Works in conjunction with the Mod 7 Python publisher
  * Mod2-3-6-7 Directory
  
* To execute the client code perform the following;
  * In the root, open a terminal and type chmod 700 Start_IOT-Dashboard.sh ,  select enter
  * Now, type ./Start_IOT-Dashboard.sh
  * You should see Meteor start in the terminal
    ** This assumes you have Mongo running external from Meteor, this property is set in the package.json (top line, Start)
    ** If this is not your setup, Do not use this script, run meteor from inside the client dir by typing 'meteor"
  
## Node-Red Flows
All Node-Red flows can be found in the flows directory as .json files and labled

* All Flows can be imported into your Node-Red server.

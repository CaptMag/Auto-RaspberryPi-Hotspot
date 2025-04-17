# Auto-RaspberryPi-Hotspot
This script is designed to fully automate the process of turning a Raspberry Pi into a working Access Point

## Overview

Currently the script is created to check for the hardware requirements of the Raspberry Pi as well as automatically install `hostapd` and `dnsmasq`
The file sets up dnsmasq and hostapd files as well as a way to customize how you want the Access Point to be created

## Current Standings

|Task|Progress|Issues|
|----|--------|------|
|Auto-Config|Ongoing|Better Organization needed and any problems need to be resolved|
|Pre-requisites|Completed|No Issues|
|Uninstallation|Completed|No Issues|
|Debugging|Completed|No Issues|
|Error-Checker|Ongoing|May be merged in with Debugging|
|Documentation|Ongoing|No Issues|
|LLM Support|Ongoing|LLM needed and proper user functionality|

# Testing Phase

As of right now there are some current problems when it comes to the code
   1. Command Line Injection is currently applicable due to improper security checks
   2. Organization is lacking, lack of comments, explanations, imporper use of functions and excess clutter
   3. Network Manager is missing attributes from Hotspot Setup Script
   4. Some statements must be validated and should execute an error message if statement does not meet criteria
   5. password strength checker must be applied as well as removing it as plain text

Some resolved issues:

WiFi Adapter checker is currently improved to use `nmcli device status` to check if a user has at least 2 wifi adpaters no matter what they are named  
More comments have been made to some files to further explain its uses and how it works  
errors revolving around compatibility have been fixed  
Network Manager, Hotspot Setup, Menu, Uninstall, Check Configurations, and Compatibility have been vastly re-organized  

## Newly found issue

When running the initial installtion script, some lines in the Menu program do not have the given attributes from HotspotSetup.py

![image](https://github.com/user-attachments/assets/c988b21a-9b93-45cd-80c7-140a6c559976)

Currently being resolved to properly be able to run the script

## Future Goals

Currently a UnitTest is required in order to intialize any ongoing problems as well as making sure everything is working as intended  
Next on the list is to ensure parameters are met and to see if the code can "break"

## Running Program

If anyone is interested to run this program you must run this command on your Raspberry Pi Terminal  
`https://github.com/CaptMag/Auto-RaspberryPi-Hotspot.git`  
This will download all the needed files, however due to not being complete, this is just here for show honestly.

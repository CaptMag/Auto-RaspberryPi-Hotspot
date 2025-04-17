import platform
import subprocess
import sys
import time

def prereq():
    system = platform.system()

    # Makes sure the running OS is Linux and not Windows

    print('\n Executing Compatibility Script... \n')
    time.sleep(2)

    if system == "Linux":
        print("Script is compatible with Linux!")
        time.sleep(2)
    elif system == 'Windows':
        print('Script is not compatible with Windows')
        sys.exit(0)

    print("Checking for required hardware...")
    time.sleep(2)

    # Runs current device status

    try:
        devices = subprocess.check_output(['nmcli', 'device', 'status'])
        devices = devices.decode('utf-8').replace("\r", "")
        count = 0
    
        # Skip the header line
        lines = devices.splitlines()
        for i, line in enumerate(lines):
            if i == 0:
                continue

            # checks if the TYPE column `columns[1]` contains either "wifi"
            
            columns = line.split()
            if len(columns) >= 2 and columns[1] in ["wifi"]:
                count += 1 # Increment if condition is true
    
        if count >= 2:
            print(f"RPI has {count} WiFi Adapters")
            time.sleep(2)
            print(f"RPI can be configured into an Access Point!")
            time.sleep(3)
        elif count == 1:
            print(f"RPI must have 1 more Wi-Fi adapter")
        else:
            print(f"No Wi-Fi adapter found!")
            

    except subprocess.CalledProcessError:
        print("Error reading Wi-Fi devices.")



# Ensures both hostapd and dnsmasq have been successfully installed

def app_status():
    try:
        # Run commands to check if applications are installed
        subprocess.run(['hostapd', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        subprocess.run(['dnsmasq', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        
        # If we get here without exceptions, both commands succeeded
        print("Hostapd and Dnsmasq are updated and ready!")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        # One or both applications are not installed or have issues
        print("Hostapd and/or Dnsmasq are not properly installed.")
        return False

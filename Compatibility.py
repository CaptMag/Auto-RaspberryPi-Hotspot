import platform
import subprocess
import sys

def prereq():
    system = platform.system()

    if system == "Linux":
        print("Script is compatible with Linux!")
    elif system == 'Windows':
        print('Script is not compatible with Windows')
        sys.exit(0)

    print("Checking for required hardware...")

    try:
        devices = subprocess.check_output(['iw', 'dev'])
        devices = devices.decode('utf-8').replace("\r", "")

        if "wlan0" in devices and "wlan1" in devices:
            print("RPI can be configured into an AP!")
        elif "wlan0" in devices:
            print("RPI must have 1 more Wi-Fi adapter")
        else:
            print("No Wi-Fi adapter found!")

    except subprocess.CalledProcessError:
        print("Error reading Wi-Fi devices.")

def app_status():
    try:
        subprocess.run(['hostapd', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        subprocess.run(['dnsmasq', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

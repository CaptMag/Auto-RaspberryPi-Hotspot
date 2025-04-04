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

    devices = subprocess.check_output(['wlan', 'iw', 'dev', 'show', 'network'])

    devices = devices.decode('ascii')
    devices = devices.replace("\r","")

    print(devices)

    if "wlan0" in devices and "wlan1" in devices:
        print("RPI can be configured into an AP!")
    elif devices == ('wlan0'):
        print("RPI must have 1 more Wi-Fi Adapter")
    else:
        print("No Wi-Fi adpater found!")

def app_status():
    try:
        subprocess.run(['hostapd', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        subprocess.run(['dnsmasq', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False
    

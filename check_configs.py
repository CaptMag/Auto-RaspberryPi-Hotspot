import os
import time

def check_config_files():

    print('\n Checking For File Integrity \n')

    hostapd = '/etc/hostapd/hostapd.conf'
    dnsmasq = '/etc/dnsmasq.conf'

    hostapd_exists = os.path.exists(hostapd)
    dnsmasq_exists = os.path.exists(dnsmasq)

    if hostapd_exists and dnsmasq_exists:
        print("Both hostapd.conf and dnsmasq.conf are successfully created!")
        time.sleep(3)
    else:
        print("Error! One or both files do not exist!")
        time.sleep(3)

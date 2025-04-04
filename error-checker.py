import os

def check_config_files():
    hostapd = '/etc/hostapd/hostapd.conf'
    dnsmasq = '/etc/dnsmasq.conf'

    hostapd_exists = os.path.exists(hostapd)
    dnsmasq_exists = os.path.exists(dnsmasq)

    if hostapd_exists and dnsmasq_exists:
        print("Both hostapd.conf and dnsmasq.conf are successfully created!")
    else:
        print("Error! One or both files do not exist!")

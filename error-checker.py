import os

hostapd = '/ext/hostapd/hostapd.conf'
dnsmasq = '/etc/dnsmasq.conf'

hostapd_exists = os.path.exists(hostapd)
dnsmasq_exists = os.path.exists(dnsmasq)


if hostapd_exists and dnsmasq_exists:
    print("Both Hostapd.conf and Dnsmasq.conf are successfully created!")
else:
    print("Error! one or both files do not exist!")

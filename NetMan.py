from pathlib import Path
from subprocess import run
from SysConf import configure_hostapd, configure_dnsmasq, setup_iptables

def configure_network(name, GHz, Channel, Password, IPv4, country, route):
    print("\nStarting System Execution...\n")
    run("sudo apt update && sudo apt install -y dnsmasq hostapd iptables", shell=True)


    run(f"sudo nmcli con add type wifi ifname wlan0 mode ap con-name {name} ssid {name}", shell=True)
    run(f"sudo nmcli con modify {name} ipv4.addresses {IPv4}", shell=True)
    run(f"sudo nmcli con modify {name} ipv4.method manual", shell=True)
    run(f"sudo nmcli con modify MyHotspot 802-11-wireless.band {GHz}", shell=True)
    run(f"sudo nmcli con modify MyHotspot 802-11-wireless.channel {Channel}", shell=True)
    run("sudo nmcli con modify MyHotspot wifi-sec.key-mgmt wpa-psk", shell=True)
    run(f"sudo nmcli con modify MyHotspot wifi-sec.psk {Password}", shell=True)
    run(f"sudo nmcli con up {name}", shell=True)
    run("ip addr show wlan0", shell=True)

    configure_hostapd(name, GHz, Channel, Password, country)
    configure_dnsmasq(IPv4, route)
    setup_iptables()

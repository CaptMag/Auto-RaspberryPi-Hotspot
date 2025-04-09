from pathlib import Path
from subprocess import run, CalledProcessError, PIPE
from SysConf import configure_hostapd, configure_dnsmasq, setup_iptables

def configure_network(name, GHz, Channel, Password, IPv4, country, route):

    try:
        print("\nStarting System Execution...\n")

        print("Installing Required Packages...")
        run("sudo apt update && sudo apt install -y dnsmasq hostapd iptables", shell=True, check=True, stdout=PIPE, stderr=PIPE)

        print(f"Creating Wireless Access Point '{name}'...")
        run(f"sudo nmcli con add type wifi ifname wlan0 mode ap con-name {name} ssid {name}", shell=True, check=True, stdout=PIPE, stderr=PIPE)

        print("Configruing IPv4 Settings...")
        run(f"sudo nmcli con modify {name} ipv4.addresses {IPv4}", shell=True, check=True, stdout=PIPE, stderr=PIPE)
        run(f"sudo nmcli con modify {name} ipv4.method manual", shell=True, check=True, stdout=PIPE, stderr=PIPE)

        print("Configuring Wireless Settings...")
        run(f"sudo nmcli con modify {name} 802-11-wireless.band {GHz}", shell=True, check=True, stdout=PIPE, stderr=PIPE)
        run(f"sudo nmcli con modify {name} 802-11-wireless.channel {Channel}", shell=True, check=True, stdout=PIPE, stderr=PIPE)

        print("Configuring Wireless Security...")
        run("sudo nmcli con modify {name} wifi-sec.key-mgmt wpa-psk", shell=True, check=True, stdout=PIPE, stderr=PIPE)
        run(f"sudo nmcli con modify {name} wifi-sec.psk {Password}", shell=True, check=True, stdout=PIPE, stderr=PIPE)

        print("Activating connection '{name}'...")
        run(f"sudo nmcli con up {name}", shell=True, check=True, stdout=PIPE, stderr=PIPE)

        print("Network Interface Status:")
        run("ip addr show wlan0", shell=True, check=True, stdout=PIPE, stderr=PIPE)


        print("Setting up System Configurations...")
        configure_hostapd(name, GHz, Channel, Password, country)
        configure_dnsmasq(IPv4, route)
        setup_iptables()

        print(f"Hotspot {name} has been successfully created!")
        return True

    except CalledProcessError as e:
        print(f"Error during network configuration: {e}")
        return False

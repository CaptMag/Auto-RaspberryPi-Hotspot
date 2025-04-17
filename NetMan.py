import time
from subprocess import run, CalledProcessError, PIPE
from SysConf import configure_hostapd, configure_dnsmasq, setup_iptables

# Designed to setup the RPI in a proper Access Point using the information taken from SysConf.py

def configure_network(name, GHz, Channel, Password, IPv4, country, route):

    try:
        print("\nStarting System Execution...\n")

        # Instalss DNSmasq, Hostapd, and IPtables

        print("Installing Required Packages...")
        run("sudo apt update && sudo apt install -y dnsmasq hostapd iptables", shell=True, check=True, stdout=PIPE, stderr=PIPE)

        # Using users chosen name, it uses wlan0 to turn it into an Access Point

        print(f"Creating Wireless Access Point '{name}'...")
        time.sleep(2)
        run(f"sudo nmcli con add type wifi ifname wlan0 mode ap con-name {name} ssid {name}", shell=True, check=True, stdout=PIPE, stderr=PIPE)

        # Configures the IPv4 Subnet settings

        print("Configruing IPv4 Settings...")
        time.sleep(2)
        run(f"sudo nmcli con modify {name} ipv4.addresses {IPv4}", shell=True, check=True, stdout=PIPE, stderr=PIPE)
        run(f"sudo nmcli con modify {name} ipv4.method manual", shell=True, check=True, stdout=PIPE, stderr=PIPE)

        # Ensures that the correct wireless band strength corresponds with the user's selected channel using the IEEE 802.11 standards

        print("Configuring Wireless Settings...")
        time.sleep(2)
        run(f"sudo nmcli con modify {name} 802-11-wireless.band {GHz}", shell=True, check=True, stdout=PIPE, stderr=PIPE)
        run(f"sudo nmcli con modify {name} 802-11-wireless.channel {Channel}", shell=True, check=True, stdout=PIPE, stderr=PIPE)

        # Configures AP to use WPA2 (minimum security) As well as setting up the password

        print("Configuring Wireless Security...")
        time.sleep(2)
        run(f"sudo nmcli con modify {name} wifi-sec.key-mgmt wpa-psk", shell=True, check=True, stdout=PIPE, stderr=PIPE)
        run(f"sudo nmcli con modify {name} wifi-sec.psk {Password}", shell=True, check=True, stdout=PIPE, stderr=PIPE)

        # Activates and Starts the Access Point

        print(f"Activating connection '{name}'...")
        time.sleep(2)
        run(f"sudo nmcli con up {name}", shell=True, check=True, stdout=PIPE, stderr=PIPE)

        # Shows the ip address pof wlan0 (or any selected interface) to ensure it matches with users given IPv4 Address

        print("Network Interface Status:")
        time.sleep(2)
        run("ip addr show wlan0", shell=True, check=True, stdout=PIPE, stderr=PIPE)


        # Using information from SysConf.py it setups DNSmasq and Hostapd files which creates the Route, DHCP range, proper drivers, security, password integrity, SSID and more.

        print("Setting up System Configurations...")
        time.sleep(2)
        configure_hostapd(name, GHz, Channel, Password, country)
        configure_dnsmasq(IPv4, route)
        setup_iptables()

        # If successful, Access Point will be properly created

        print(f"Hotspot {name} has been successfully created!")
        return True
    
    # If not, the program will print out an error

    except CalledProcessError as e:
        print(f"Error during network configuration: {e}")
        return False

import os
import argparse
import subprocess
import sys
from pathlib import Path

def menu():
    print("What would you like to do?")
    print("[1] Create a Raspberry-Pi Hotspot")
    print("[2] Debug Raspberry-Pi")
    print("[3] Uninstall Hotspot")

def custom():
    name = input("Enter SSID Name: ")
    GHz = input("Choose g for 2.4 GHz, a for 5, ad for 60: ")
    Channel = input("For 2.4 GHz choose channels 1-11, 5 GHz choose 36, 40, 44, 48, 60 GHz choose 1-4:  ")
    Password = input("Create a valid and secure password: ")
    IPv4 = input("Enter the IPv4 subnet you wish to use: ")
    country = input("Enter your country code (example: US, FR, UK, etc.): ")
    route = input("Enter Default Gateway: ")

    def NetworkManager():
        print("\nStarting System Execution...\n")
        subprocess.run(["sudo apt install dnsmasq -y", "sudo apt install hostapd -y", "sudo apt install iptables -y"])
        subprocess.run(["sudo nmcli con add type wifi ifname wlan0 mode ap con-name" + name + "ssid" + name,
                                "sudo nmcli con modify" + name + "ipv4.addresses" + IPv4,
                                "sudo nmcli con modify" + name + "ipv4.method manual", 
                                "sudo nmcli con modify MyHotspot 802-11-wireless.band" + GHz,
                                "sudo nmcli con modify MyHotspot 802-11-wireless.channel" + Channel,
                                "sudo nmcli con modify MyHotspot wifi-sec.key-mgmt wpa-psk",
                                "sudo nmcli con modify MyHotspot wifi-sec.psk" + Password])
        subprocess.run("sudo nmcli con up" + name)
        subprocess.run("ip addr show wlan0")

        def hostapd():
            hostapd = Path("/etc/hostapd/hostapd.conf")
            hostapdlist = [f"""
            interface=wlan0
            driver=nl80211
            ssid={name}
            hw_mode={GHz}
            channel={Channel}
            wmm_enabled=1
            auth_algs=1
            wpa=2
            wpa_key_mgmt=WPA-PSK #edit
            rsn_pairwise=CCMP
            wpa_passphrase={Password}
            ieee80211d=1
            ieee80211h=1
            country_code={country}
            """
            ]
            hostapd.write_text("\n" .join(hostapdlist) + "\n")


            config = Path("/etc/default/hostapd")
            with config.open('a') as file:
                file.write('\nDAEMON_CONF="/etc/hostapd/hostapd.conf"\n')  

                def IP_modify(ip_address, new_value):
                    IPv4 = ip_address.split(".")  

                    if len(IPv4) == 4 and IPv4[2].isdigit():
                        IPv4[2] = str(new_value)
                        return ".".join(IPv4)

                    return "Invalid IP Address"  

                ip = IPv4
                more_ip = IP_modify(more_ip, 30)            
                
                def dnsmasq():
                    subprocess.run("sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.backup")
                    dns = Path("/etc/dnsmasq.conf")
                    dnsmasq = [f"""
                        interface=wlan0
                        dhcp-range={IPv4},{more_ip},12h
                        dhcp-option=3,{route}
                        dhcp-option=6,{route}
                    """]
                    
                    def iptable_setup():
                        subprocess.run(["sudo sysctl -w net.ipv4.ip_forward=1", "echo ""net.ipv4.ip_forward=1"" | sudo tee -a /etc/sysctl.conf"])
                        subprocess.run(["sudo iptables -t nat -A POSTROUTING -o wlan1 -j MASQUERADE",
                                        "sudo iptables -A FORWARD -i wlan1 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT",
                                        "sudo iptables -A FORWARD -i wlan0 -o wlan1 -j ACCEPT",
                                        "sudo netfilter-persistent save"])
                        
                        def finale():
                            subprocess.run(["sudo systemctl unmask hostapd",
                                        "sudo systemctl enable hostapd",
                                        "sudo systemctl enable dnsmasq",
                                        "sudo systemctl start hostapd",
                                        "sudo systemctl start dnsmasq",
                                        "sudo systemctl status hostapd",
                                        "sudo systemctl status dnsmasq"])
    
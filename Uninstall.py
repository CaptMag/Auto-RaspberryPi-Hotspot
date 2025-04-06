# uninstall.py
import subprocess
import sys
import os

def uninstall_hotspot():
    while True:
        question = input("Would you really like to uninstall everything? (yes/no): ").strip().lower()

        if question == 'yes':
            print("Stopping Services...")
            subprocess.run(["sudo", "systemctl", "stop", "hostapd"], check=True)
            subprocess.run(["sudo", "systemctl", "stop", "dnsmasq"], check=True)

            print("Removing Packages...")
            subprocess.run(["sudo", "apt", "purge", "-y", "hostapd"], check=True)
            subprocess.run(["sudo", "apt", "purge", "-y", "dnsmasq"], check=True)

            print("Removing Configuration Files...")

            hostapd = "/etc/hostapd/hostapd.conf"
            dnsmasq = "/etc/dnsmasq.conf"

            if os.path.exists(hostapd):
                subprocess.run(["sudo", "rm", "-rf", "/etc/hostapd/hostapd.conf"], check=True)
            if os.path.exists(dnsmasq):
                subprocess.run(["sudo", "rm", "-rf", "/etc/dnsmasq.conf"], check=True)
            
            print("Uninstallation complete.")
            break
        elif question == 'no':
            print("Uninstallation terminated.")
            return
        else:
            print("Error! No valid answer provided!")

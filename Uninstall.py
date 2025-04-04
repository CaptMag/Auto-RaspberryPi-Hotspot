import subprocess
import sys

def uninstall_hotspot():
    while True:
        question = input("Would you really like to uninstall everything? (yes/no): ").strip().lower()

        if question == 'yes':
            subprocess.run(["sudo", "systemctl", "stop", "hostapd"])
            subprocess.run(["sudo", "systemctl", "stop", "dnsmasq"])
            subprocess.run(["sudo", "apt", "purge", "-y", "hostapd"])
            subprocess.run(["sudo", "apt", "purge", "-y", "dnsmasq"])
            subprocess.run(["sudo", "rm", "-rf", "/etc/hostapd/hostapd.conf"])
            subprocess.run(["sudo", "rm", "-rf", "/etc/dnsmasq.conf"])
            print("Uninstallation complete.")
            break
        elif question == 'no':
            print("Uninstallation terminated.")
            sys.exit()
        else:
            print("Error! No valid answer provided!")

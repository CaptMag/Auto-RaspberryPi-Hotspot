# uninstall.py
import subprocess
import time
import os

def uninstall_hotspot():
    while True:
        question = input("Would you really like to uninstall everything? (yes/no): ").strip().lower()

        if question == 'yes':
            print("\nStopping Services... \n")
            time.sleep(2)
            subprocess.run(["sudo", "systemctl", "disable", "hostapd"], check=True) # Disables both Hostapd and Dnsmasq
            subprocess.run(["sudo", "systemctl", "disable", "dnsmasq"], check=True)

            print("Removing Packages...")
            time.sleep(2)
            subprocess.run(["sudo", "apt", "purge", "-y", "hostapd"], check=True) # Purges [removes] both applications
            subprocess.run(["sudo", "apt", "purge", "-y", "dnsmasq"], check=True)

            print("\nRemoving Configuration Files... \n")

            hostapd = "/etc/hostapd/hostapd.conf"
            dnsmasq = "/etc/dnsmasq.conf"

            if os.path.exists(hostapd):
                subprocess.run(["sudo", "rm", "-rf", "/etc/hostapd/hostapd.conf"], check=True) # Deletes both files with root privilege
            if os.path.exists(dnsmasq):
                subprocess.run(["sudo", "rm", "-rf", "/etc/dnsmasq.conf"], check=True)


            print("\n Removing Network Manager Configurations... \n")

            result = subprocess.run(["nmcli", "-t", "connection", "show"], capture_output=True, text=True) # Checks to see current network manager command line connections
            for line in result.stdout.splitlines():
                if "wifi" in line and "ap" in line:
                    conn_name = line.split(":")[0]
                    subprocess.run(["sudo", "nmcli", "connection", "delete", conn_name], check=False) # If an Access Point already exists, delete it


            print("\n Resetting Network Forwarding... \n")
            subprocess.run(["sudo", "sysctl", "-w", "net.ipv4.ip.forward=0"], check=False) # Sets IP forwarding back to default (false)


            print("\n Cleaning Firewall Rules... \n")
            subprocess.run(["sudo", "iptables", "-F"], check=False)
            subprocess.run(["sudo", "iptables", "-t", "nat", "-F"], check=False) # Cleans any IPtables (firewall) rules

            
            print("Uninstallation complete.")
            time.sleep(1)
            break
        elif question == 'no':
            print("Uninstallation terminated.")
            time.sleep(1)
            return
        else:
            print("Error! No valid answer provided!")
            time.sleep(1)

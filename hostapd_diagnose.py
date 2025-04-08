import subprocess
from pathlib import Path
import re

def hostapd_issues():
    result = subprocess.run(["sudo", "hostapd", "-dd", "/etc/hostapd/hostapd.conf"], capture_output=True, text=True, stderr=subprocess.STDOUT)
    output = result.stdout.lower()

    if "could not read interface: no such device" in output:
        print("Fixing interface issues...")
        wlan_up = subprocess.run(["sudo", "ip", "link", "set", "wlan0", "up"], capture_output=True, text=True, check=False)
    
        if wlan_up.returncode == 0:
            print("Interface wlan0 is now up")
            return "Done"
        else:
            print(f"Failed to bring up wlan0: ")
            return "Failed"

    elif "nl80211: could not configure driver mode" in output:
        print("Fixing driver mode issues...")
        subprocess.run(["sudo", "apt", "install", "-y", "iw", "wireless-tools"], capture_output=True, text=True, check=False)
        iw_list = subprocess.run(["bash", "-c", "iw list | grep 'AP'"], capture_output=True, text=True, check=False)
        if "AP" in iw_list.stdout:
            print("Your wireless card support AP mode")
            return "Done"
        else:
            print("Your wireless card does not support AP mode")
            return "Failed"

    elif "invalid/unknown driver ‘nl80211’" in output:
        print("Fixing incorrect driver in hostapd.conf...")
        hostapd = Path("/etc/hostapd/hostapd.conf")
        if hostapd.exists():
            with hostapd.open("a") as f:
                f.write("\ndriver=nl80211\n")

    elif "failed to start hostapd.service: unit hostapd.service not found" in output:
        try:
            print("Fixing hostapd service not found...")
            subprocess.run(["sudo", "apt", "install", "-y", "hostapd"], capture_output=True, text=True, check=False)
            subprocess.run(["sudo", "systemctl", "enable", "hostapd"], capture_output=True, text=True, check=False)
            subprocess.run(["sudo", "systemctl", "start", "hostapd"], capture_output=True, text=True, check=False)
        except subprocess.CalledProcessError as e:
            print(f"Error Detected during starting: {e}")

    elif "ioctl[SIOCSIWMODE]: Operation not permitted" in output:
            print("Fixing Operation Permissions...")
            op_perm = subprocess.run(["sudo", "systemctl", "start", "hostapd"])
            if op_perm.returncode == 0:
                print("Hostapd succesfully ran with sudo!")
                return "Done"
            else:
                print("Hostapd couldn't be ran with admin permission")
                return "Failed"

    else:
        print("No known issues detected.")
        print("\nCurrent wireless status:")
        subprocess.run(["iwconfig"], check=False)
        print("\nHostapd configuration:")
        subprocess.run(["cat", "/etc/hostapd/hostapd.conf"], check=False)

    return "Done"

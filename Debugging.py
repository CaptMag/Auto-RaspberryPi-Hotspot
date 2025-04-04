import subprocess
from pathlib import Path

def hostapd_issues():
    result = subprocess.run(["sudo", "hostapd", "-dd", "/etc/hostapd/hostapd.conf"], capture_output=True, text=True, stderr=subprocess.STDOUT)
    output = result.stdout.lower()
    
    if "Could not read interface: No such device" in output:
        print("Fixing Interface Issues...")
        return subprocess.run(["sudo", "ip", "link", "set", "wlan0", "up"])
    
    elif "nl80211: Could not configure driver mode" in output:
        print("Fixing Driver Mode Issues...")
        subprocess.run(["sudo", "apt", "install", "-y", "iw", "wireless-tools"])
        return subprocess.run(["bash", "-c", "iw list | grep 'AP'"])
    
    elif "Invalid/unknown driver ‘nl80211’" in output:
        print("Fixing Incorrect Driver In Hostapd.conf...")
        hostapd = Path("/etc/hostapd/hostapd.conf")
        if hostapd.exists():
            with hostapd.open("a") as f:
                f.write("\ndriver=nl80211\n")

    elif "Failed to start hostapd.service: Unit hostapd.service not found" in output:
        print("Fixing Hostapd Service Not Found...")
        subprocess.run(["sudo", "apt", "install", "-y", "hostapd"])
        subprocess.run(["sudo", "systemctl", "enable", "hostapd"])
        subprocess.run(["sudo", "systemctl", "start", "hostapd"])

    else:
        print("No known issues detected.")


    return "Done"
    
print(hostapd_issues())

import subprocess
from pathlib import Path

def hostapd_issues():
    result = subprocess.run(["sudo", "hostapd", "-dd", "/etc/hostapd/hostapd.conf"], capture_output=True, text=True, stderr=subprocess.STDOUT)
    output = result.stdout.lower()

    if "could not read interface: no such device" in output:
        print("Fixing interface issues...")
        return subprocess.run(["sudo", "ip", "link", "set", "wlan0", "up"])

    elif "nl80211: could not configure driver mode" in output:
        print("Fixing driver mode issues...")
        subprocess.run(["sudo", "apt", "install", "-y", "iw", "wireless-tools"])
        return subprocess.run(["bash", "-c", "iw list | grep 'AP'"])

    elif "invalid/unknown driver ‘nl80211’" in output:
        print("Fixing incorrect driver in hostapd.conf...")
        hostapd = Path("/etc/hostapd/hostapd.conf")
        if hostapd.exists():
            with hostapd.open("a") as f:
                f.write("\ndriver=nl80211\n")

    elif "failed to start hostapd.service: unit hostapd.service not found" in output:
        print("Fixing hostapd service not found...")
        subprocess.run(["sudo", "apt", "install", "-y", "hostapd"])
        subprocess.run(["sudo", "systemctl", "enable", "hostapd"])
        subprocess.run(["sudo", "systemctl", "start", "hostapd"])

    else:
        print("No known issues detected.")

    return "Done"

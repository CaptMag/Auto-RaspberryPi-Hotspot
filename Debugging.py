import platform
import psutil
import subprocess
import time
import os
import sys
from pathlib import Path

def hostapd_issues():
    result = subprocess.run(["sudo", "hostapd", "-dd", "/etc/hostapd/hostapd.conf"], capture_output=True, text=True, stderr=subprocess.STDOUT)
    output = result.stdout.lower()
    
    if "Could not read interface [interface]: No such device" in output:
        return subprocess.run(["sudo ip link set wlan0 up"])
    elif "nl80211: Could not configure driver mode" in output:
        subprocess.run(["sudo apt install iw wireless-tools"])
        return subprocess.run(["iw list | grep 'AP'"])
    elif "Invalid/unknown driver ‘nl80211’" in output:
        hostapd = Path("/etc/hostapd/hostapd.conf")
        hostapddebug = [f"driver=nl80211"]
    elif "Failed to start hostapd.service: Unit hostapd.service not found" in output:
        return subprocess.run(["""
            sudo apt install hostapd
            sudo systemctl enable hostapd
            sudo systemctl start hostapd
            """])
    
print(hostapd_issues)
import subprocess
from pathlib import Path

def install_packages():
    packages = ["dnsmasq", "hostapd", "iptables"]
    for pkg in packages:
        subprocess.run(["sudo", "apt", "install", "-y", pkg], check=True)

def enable_ip_forwarding():
    subprocess.run(["sudo", "sysctl", "-w", "net.ipv4.ip_forward=1"], check=True)
    with open("/etc/sysctl.conf", "a") as f:
        f.write("\nnet.ipv4.ip_forward=1\n")

def write_hostapd_config(ssid, password, channel, band, country):
    config = f"""
interface=wlan0
driver=nl80211
ssid={ssid}
hw_mode={band}
channel={channel}
wmm_enabled=1
auth_algs=1
wpa=2
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
wpa_passphrase={password}
ieee80211d=1
ieee80211h=1
country_code={country}
"""
    Path("/etc/hostapd/hostapd.conf").write_text(config.strip() + "\n")
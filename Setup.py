from utils import run_cmd

def configure_hotspot(ssid, password, ip):
    run_cmd(["sudo", "nmcli", "con", "add", "type", "wifi", "ifname", "wlan0", "mode", "ap", "con-name", ssid, "ssid", ssid])
    run_cmd(["sudo", "nmcli", "con", "modify", ssid, "wifi-sec.key-mgmt", "wpa-psk"])
    run_cmd(["sudo", "nmcli", "con", "modify", ssid, "wifi-sec.psk", password])
    run_cmd(["sudo", "nmcli", "con", "modify", ssid, "ipv4.addresses", f"{ip}/24"])

from pathlib import Path
from subprocess import run

def configure_hostapd(name, GHz, Channel, Password, country):
    hostapd_conf = Path("/etc/hostapd/hostapd.conf")
    content = f"""
interface=wlan0
driver=nl80211
ssid={name}
hw_mode={GHz}
channel={Channel}
wmm_enabled=1
auth_algs=1
wpa=2
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
wpa_passphrase={Password}
ieee80211d=1
ieee80211h=1
country_code={country}
"""
    hostapd_conf.write_text(content)

    with Path("/etc/default/hostapd").open("a") as f:
        f.write('\nDAEMON_CONF="/etc/hostapd/hostapd.conf"\n')

def configure_dnsmasq(ip_start, route):
    def modify_ip(ip, new_value):
        parts = ip.split(".")
        if len(parts) == 4 and parts[2].isdigit():
            parts[2] = str(new_value)
            return ".".join(parts)
        return ip

    ip_end = modify_ip(ip_start, 30)
    run("sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.backup", shell=True)
    dns_conf = Path("/etc/dnsmasq.conf")
    dns_conf.write_text(f"""
interface=wlan0
dhcp-range={ip_start},{ip_end},12h
dhcp-option=3,{route}
dhcp-option=6,{route}
""")

def setup_iptables():
    run("sudo sysctl -w net.ipv4.ip_forward=1", shell=True)
    run("echo \"net.ipv4.ip_forward=1\" | sudo tee -a /etc/sysctl.conf", shell=True)
    run("sudo iptables -t nat -A POSTROUTING -o wlan1 -j MASQUERADE", shell=True)
    run("sudo iptables -A FORWARD -i wlan1 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT", shell=True)
    run("sudo iptables -A FORWARD -i wlan0 -o wlan1 -j ACCEPT", shell=True)
    run("sudo netfilter-persistent save", shell=True)

    run("sudo systemctl unmask hostapd", shell=True)
    run("sudo systemctl enable hostapd", shell=True)
    run("sudo systemctl enable dnsmasq", shell=True)
    run("sudo systemctl start hostapd", shell=True)
    run("sudo systemctl start dnsmasq", shell=True)
    run("sudo systemctl status hostapd", shell=True)
    run("sudo systemctl status dnsmasq", shell=True)

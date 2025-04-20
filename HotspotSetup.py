from NetMan import configure_network
import ipaddress

def setup_hotspot():

    while True:
        name = input("Enter SSID Name: ")
        if name:
            break


    valid_bands = ["g", "a", "ad"]
    while True:
       GHz = input("Choose g for 2.4 GHz, a for 5, ad for 60: ")
       if GHz in valid_bands:
           break
       print(f"Invalid band. Please choose from: {', '.join(valid_bands)}")

    while True:
        Channel = input("For 2.4 GHz choose channels 1-11, 5 GHz choose 36, 40, 44, 48, 60 GHz choose 1-4: ")
        if validate_channel(GHz, Channel):
            break

    Password = input("Create a valid and secure password: ")

    while True:
        IPv4 = input("Enter the IPv4 subnet you wish to use (e.g., 192.168.1.0/24): ")
        if IPv4_subnet(IPv4):
            break

    country = input("Enter your country code (example: US, FR, UK, etc.): ")

    while True:
        route = input("Enter Default Gateway: ")
        try:
            ipaddress.IPv4Address(route)
            break
        except ValueError:
            print("Invalid Gateway IP Address")


    configure_network(name, GHz, Channel, Password, IPv4, country, route)

def validate_channel(GHz, channel):
    try:
        channel = int(channel)
        if GHz == "g" and 1 <= channel <= 11:
            return True
        elif GHz == "a" and channel in [36, 40, 44, 48]:
            return True
        elif GHz == "ad" and 1 <= channel <= 4:
            return True
        else:
            print(f"Error! Improper {channel} for {GHz} Provided")
            return False
    except ValueError:
        print("Channel must be a number")
        return False
    
def IPv4_subnet(subnet):
    try:

        if "/" not in subnet:
            print("Error: IP subnet must be in CIDR notation (e.g., 192.168.1.0/24)")
            return False

        ipaddress.IPv4Network(subnet, strict=False)
        return True
    except ValueError as e:
        print(f"Invalid IPv4 subnet: {e}")
        return False

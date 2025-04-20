from NetMan import configure_network
import ipaddress

def setup_hotspot():

    while True:
        name = input("Enter SSID Name: ") # Input Access Point Name
        if name:
            break


    valid_bands = ["g", "a", "ad"]
    while True:
       GHz = input("Choose g for 2.4 GHz, a for 5, ad for 60: ") # Different strength's depending on selected band
       if GHz in valid_bands:
           break
       print(f"Invalid band. Please choose from: {', '.join(valid_bands)}")

    nmcli_band = GHz
    if GHz == "g":
        nmcli_band = "bg"

    while True:
        Channel = input("For 2.4 GHz choose channels 1-11, 5 GHz choose 36, 40, 44, 48, 60 GHz choose 1-4: ") # Channel cooresponding to selected band
        if validate_channel(GHz, Channel):
            break

    Password = input("Create a valid and secure password: ") # Password verification

    while True:
        IPv4 = input("Enter the IPv4 subnet you wish to use (e.g., 192.168.1.0/24): ") # Valid CIDR IP Address
        if IPv4_subnet(IPv4):
            break

    country = input("Enter your country code (example: US, FR, UK, etc.): ") # Country Code

    while True:
        route = input("Enter Default Gateway: ") # Default Gateway for Devices that connect to the AP
        try:
            ipaddress.IPv4Address(route)
            break
        except ValueError:
            print("Invalid Gateway IP Address")

    return_values = (name, GHz, nmcli_band, Channel, Password, IPv4, country, route) # Ensure values are correct
    print(f"Returning: {return_values}")

    configure_network(name, GHz, Channel, Password, IPv4, country, route, nmcli_band) # Sends values to Netman.py
    return return_values


def validate_channel(GHz, channel): # Ensure correct channel is chosen
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
    
def IPv4_subnet(subnet): # Ensures proper IPv4 CIDR format is intiated
    try:

        if "/" not in subnet:
            print("Error: IP subnet must be in CIDR notation (e.g., 192.168.1.0/24)")
            return False

        ipaddress.IPv4Network(subnet, strict=False)
        return True
    except ValueError as e:
        print(f"Invalid IPv4 subnet: {e}")
        return False
    
    

from NetMan import configure_network

def setup_hotspot():
    name = input("Enter SSID Name: ")
    GHz = input("Choose g for 2.4 GHz, a for 5, ad for 60: ")
    Channel = input("For 2.4 GHz choose channels 1-11, 5 GHz choose 36, 40, 44, 48, 60 GHz choose 1-4: ")
    Password = input("Create a valid and secure password: ")
    IPv4 = input("Enter the IPv4 subnet you wish to use: ")
    country = input("Enter your country code (example: US, FR, UK, etc.): ")
    route = input("Enter Default Gateway: ")

    configure_network(name, GHz, Channel, Password, IPv4, country, route)

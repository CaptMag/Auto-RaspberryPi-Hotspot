import os

def menu():
    while True:
        os.system('clear')
        print("What would you like to do?")
        print("[1] Create a Raspberry-Pi Hotspot")
        print("[2] Debug Raspberry-Pi")
        print("[3] Uninstall Hotspot")
        print("[4] Exit Menu")

        choice = input("Choose an option: ")
        if choice == "1":
            sub_choice1()
        elif choice == "2":
            sub_choice2()
        elif choice == "3":
            uninstallation()
        elif choice == "4":
            break

def sub_choice1(): # installtion functions and compatability
    os.system('clear')
    print("[1] Check for device compatability")
    print("[2] Run Installtion")
    print("[3] Exit")
    subchoice = input("Choose an option: ")
    
    if subchoice == "1":
        from Compatibility import prereq
        prereq()
    elif subchoice == "2":
        creation()
    elif subchoice == "3":
        return  # Return to main menu instead of continue

def creation():
    os.system('clear')
    from HotspotSetup import setup_hotspot
    from NetMan import configure_network
    from SysConf import configure_hostapd, configure_dnsmasq, setup_iptables
    # Get the parameters from setup_hotspot
    name, GHz, nmcli_band, Channel, Password, IPv4, country, route = setup_hotspot()
    
    # Pass them to each function that needs them
    configure_network(name, GHz, nmcli_band, Channel, Password, IPv4, country, route)
    configure_hostapd(name, GHz, Channel, Password, country)
    configure_dnsmasq(IPv4, route)
    setup_iptables()

def sub_choice2(): # Subchoice for debugging and file integrity
    os.system('clear')
    print("[1] Check for file integrity")
    print("[2] Debug Raspberry-Pi Issues")
    print("[3] Exit")
    subchoice = input("Choose an option: ")
    
    if subchoice == "1":
        check_file()
    elif subchoice == "2":
        diagnosis()
    elif subchoice == "3":
        return  # Return to main menu

def check_file():
    os.system('clear')
    from check_configs import check_config_files
    check_config_files() # runs file checker

def diagnosis():
    os.system('clear')
    from hostapd_diagnose import hostapd_issues
    hostapd_issues() # self-diagnoses hostapd issues

def uninstallation():
    os.system('clear')
    from Uninstall import uninstall_hotspot
    uninstall_hotspot() # Access Point Uninstall Script


# Call the menu function to start the program
if __name__ == "__main__":
    menu()

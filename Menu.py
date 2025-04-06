def menu():
    from HotspotSetup import setup_hotspot

    while True:
        print("What would you like to do?")
        print("[1] Create a Raspberry-Pi Hotspot")
        print("[2] Debug Raspberry-Pi")
        print("[3] Uninstall Hotspot")
        print("[4] Exit Menu")

        choice = input("Choose an option: ")
        if choice == "1":
            print("[1] Check for device compatability")
            print("[2] Run Installtion")
            print("[3] Exit")
            subchoice = input("Choose and option: ")
            if subchoice == "1":
                from Compatibility import prereq
                prereq()
            elif subchoice == "2":
                from HotspotSetup import setup_hotspot
                from NetMan import configure_network
                from SysConf import configure_hostapd, configure_dnsmasq, setup_iptables
                setup_hotspot()
                configure_network()
                configure_hostapd()
                configure_dnsmasq()
                setup_iptables()
            elif subchoice == "3":
                continue
        elif choice == "2":
            print("[1] Check for file integrity")
            print("[2] Debug Raspberry-Pi Issues")
            print("[3] Exit")
            subchoice = input("Choose an option: ")
            if subchoice == "1":
                from check_configs import check_config_files
                check_config_files()
            elif subchoice == "2":
                from hostapd_diagnose import hostapd_issues
                hostapd_issues()
            elif choice == "3":
                continue
        elif choice == "3":
            from Uninstall import uninstall_hotspot
            uninstall_hotspot()
        elif choice == "4":
            break

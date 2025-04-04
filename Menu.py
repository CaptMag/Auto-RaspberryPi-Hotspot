def menu():
    from HotspotSetup import setup_hotspot

    while True:
        print("What would you like to do?")
        print("[1] Create a Raspberry-Pi Hotspot")
        print("[2] Debug Raspberry-Pi")
        print("[3] Check For File Creation")
        print("[4] Uninstall Hotspot")
        print("[5] Exit Menu")

        choice = input("Choose an option: ")
        if choice == "1":
            from Compatibility import prereq
            prereq()
        elif choice == "2":
            from hostapd_diagnose import hostapd_issues
            hostapd_issues()
        elif choice == "3":
            from check_configs import check_config_files
            check_config_files()
        elif choice == "4":
            from Uninstall import uninstall_hotspot
            uninstall_hotspot()
        elif choice == "5":
            break

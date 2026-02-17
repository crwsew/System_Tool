def main_menu() :
    while True:
        print("\n--- System Tool ---")
        print("1. System Info")
        print("2. Process Viewer")
        print("3. File Manager")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1" :
            print("System Info selected (to implement)")

        elif choice == "2" :
            print("Process Viewer selected (to implement)")
        
        elif choice == "3" :
            print("File Manager selected (to implement)")

        elif choice == "4" :
            print("Exiting...")
            break
        else:
            print ("Invalid choice, try again.")
        
if __name__ == "__main__" :
    main_menu()
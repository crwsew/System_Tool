from system_info import display_system_info
from process_manager import display_processes, kill_process
from file_manager import list_files, create_file, delete_file, file_size
from logger import log_action

def file_manager_menu():
    print("\n--- File Manager ---")
    print("a. List files")
    print("b. Create file")
    print("c. Delete file")
    print("d. File size")
    
    sub = input("Choose option: ")

    if sub == "a":
        path = input("Enter path (default='.'): ") or "."
        list_files(path)
        log_action("Listed files")
    elif sub == "b":
        filename = input("Filename to create: ")
        create_file(filename)
        log_action(f"Created file: {filename}")
    elif sub == "c":
        filename = input("Filename to delete: ")
        delete_file(filename)
        log_action(f"Deleted file: {filename}")
    elif sub == "d":
        filename = input("Filename to check size: ")
        file_size(filename)
        log_action(f"Checked size of file: {filename}")
    else:
        print("Invalid choice")

def process_menu():
    print("\n--- Process Viewer ---")
    display_processes()
    print("k. Kill a process")
    sub = input("Choose option or press Enter to continue: ")
    if sub.lower() == "k":
        action_result = kill_process()
        log_action(action_result)

def main_menu():
    while True:
        print("\n====== System Tool ======")
        print("1. System Info")
        print("2. Process Viewer")
        print("3. File Manager")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            display_system_info()
            log_action("Viewed System Info")

        elif choice == "2":
            process_menu()
            log_action("Viewed Processes")

        elif choice == "3":
            file_manager_menu()

        elif choice == "4":
            print("Exiting...")
            log_action("Exited program")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main_menu()

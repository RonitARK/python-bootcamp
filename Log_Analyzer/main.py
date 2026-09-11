import time

def menu():
    print('''\n========== LOG ANALYZER ==========
    
        1. Show log level summary
        2. Show error summary
        3. Show user activity counts
        4. Show current user status
        5. Search logs by user
        6. Show user statistics
        7. Exit
    
        Enter your choice: ''')

def menu_log_level_summary():
    import log_level_summary as lls
                            
    print('''\nLog Summary
-----------------''')
                            
    log_levels = lls.log_level_summary()
                    
    for key, value in log_levels.items():
        print(f"{key} : {value}")
    
    print(f"\nMost Common: {max(log_levels, key=log_levels.get)}")

def menu_error_message_summary():
    import error_message_summary as ems
    
    print('''\nError Message Summary
-----------------''')
                    
    for key, value in ems.error_message_summary().items():
        print(f"{key} : {value}")

def menu_user_activity_summary():
    import user_activity_summary as uas
                            
    print('''\nUser Activity Summary
-----------------''')
                            
    for key, value in uas.user_activity_summary().items():
        print(f"{key} : {value}")

def menu_user_current_activity():
    import user_current_activity as uca
                                    
    print('''\nUser Current Activity
-----------------''')
                                    
    for key, value in uca.user_current_activity().items():
        print(f"{key} : {value}")

def menu_search_logs_by_user():
    import user_log_search as uls
                    
    print('''User LOGS SEARCH
-----------------''')
                    
    try:
        name = input("Enter the user name to search logs: ")
        if not name.isalpha():
            raise ValueError()
                    
        for log in uls.user_log_search(name):
            print(log)
                    
                    
    except ValueError:
        print(f"\nInvalid input. Please enter a valid user name.")
                    
        time.sleep(3)  # Adding a delay for better readability

def menu_user_statistics():
    import user_statistics as us
                    
    print('''\nUser STATISTICS
-----------------''')
                                
    try:
        name = input("Enter the user name to search statistics: ")
        if not name.isalpha():
            raise ValueError()
                    
        logins, logouts, total_events, current_status = us.user_statistics(name)
                    
        print(f"\nUser: {name}\n")
        print(f"Total events: {total_events}\nLogins: {logins}\nLogouts: {logouts}\nCurrentStatus: {current_status}")
                    
    except ValueError:
        print(f"\nInvalid input. Please enter a valid user name.")
                                
        time.sleep(2)  # Adding a delay for better readability


def main():
    while True:
        menu()

        try:
            choice = int(input())

            if choice < 1 or choice > 7:
                raise ValueError()

            match choice:
                case 1:
                    # LOG_LEVEL_SUMMARY
                    menu_log_level_summary()            
                    time.sleep(3)  # Adding a delay for better readability

                case 2:
                    # ERROR_MESSAGE_SUMMARY
                    menu_error_message_summary()
                    time.sleep(3)  # Adding a delay for better readability

                case 3:
                    # USER_ACTIVITY_SUMMARY
                    menu_user_activity_summary()                            
                    time.sleep(3)  # Adding a delay for better readability
                            
                case 4:
                    # USER_CURRENT_ACTIVITY
                    menu_user_current_activity()
                    time.sleep(3)  # Adding a delay for better readability

                case 5:
                    # SEARCH_LOGS_BY_USER
                    menu_search_logs_by_user()
                    time.sleep(3)  # Adding a delay for better readability

                case 6:
                    # USER STATISTICS
                    menu_user_statistics()
                    time.sleep(3)  # Adding a delay for better readability

                case 7:
                    print("\nExiting the program.")
                    break

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")

            time.sleep(3)  # Adding a delay for better readability

if __name__ == "__main__":
    main()


def user_current_activity():
    with open("Log_Analyzer/log.txt", "r") as file:

        user_dict = {}

        for line in file:
            user_data = line.split()

            if not user_data:
                continue
            
            if user_data[0] == "INFO":
                user_name = user_data[2]
                user_activity = " ".join(user_data[3:5])

                user_dict[user_name] = user_activity

    return user_dict

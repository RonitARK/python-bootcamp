import config

def user_activity_summary():
    with open(config.LOG_FILE, "r") as file:

        user_dict = {}

        for line in file:
            user_data = line.split()

            if not user_data:
                continue
            
            if user_data[0] == "INFO":
                user_name = user_data[2]
                user_activity = user_data[4]

                if user_name in user_dict:
                    if user_activity == "in":
                        user_dict[user_name]["login"] += 1
                    elif user_activity == "out":
                        user_dict[user_name]["logout"] += 1

                else:
                    user_dict[user_name] = {
                        "login": 1 if user_activity == "in" else 0,
                        "logout": 1 if user_activity == "out" else 0
                    }

    return user_dict
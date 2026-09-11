import config

def user_log_search(name):
    with open(config.LOG_FILE, "r") as file:
        log_search = []
        
        for line in file:
            log_data = line.split()
                    
            if not log_data:
                continue

            if log_data[0] == "INFO" and (log_data[2].lower() == name.lower()):
                log_search.append(line)
            else:
                continue

    if not log_search:
        return [f"No logs found for user '{name}'"]
    
    return log_search


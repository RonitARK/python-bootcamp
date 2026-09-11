
def log_level_summary():
    with open("Log_Analyzer/log.txt", "r") as file:

        log_dict = {}

        for line in file:
            log_data = line.split()
            
            if not log_data:
                continue
            else:
                log_cache = log_data[0]

            if log_cache in log_dict:
                log_dict[log_cache] += 1
            else:
                log_dict[log_cache] = 1

    return log_dict
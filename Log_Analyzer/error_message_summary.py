
def error_message_summary():
    with open("Log_Analyzer/log.txt", "r") as file:

        error_dict = {}

        for line in file:
            error_data = line.split()

            if not error_data:
                continue

            error_cache = " ".join(error_data[1:])
            
            if error_data[0] == "ERROR":
                if error_cache in error_dict:
                    error_dict[error_cache] += 1
                else:
                    error_dict[error_cache] = 1

    return error_dict

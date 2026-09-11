import user_activity_summary as uas
import user_current_activity as uca

def user_statistics(name):
    activity = uas.user_activity_summary()
    current_activity = uca.user_current_activity()

    actual_name = None

    for username in activity:
        if username.lower() == name.lower():
            actual_name = username
            break
    
    logins = activity.get(actual_name, {}).get("login", 0)
    logouts = activity.get(actual_name, {}).get("logout", 0)
    total_events = logins + logouts
    current_status = current_activity.get(actual_name, "Unknown")

    return logins, logouts, total_events, current_status

from datetime import datetime

# Function to format datetime
def format_datetime(date_str, time_str):
    datetime_str = f"{date_str} {time_str}"
    return datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")

# Function to check if event is upcoming
def is_event_upcoming(event_date):
    return datetime.now() < event_date
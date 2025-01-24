from datetime import datetime

class DateTimeInfo:
    def get_time(self):
        """Returns the current time in HH:MM:SS format."""
        return datetime.now().strftime("%H:%M:%S")
    
    def get_date(self):
        """Returns the current date in YYYY-MM-DD format."""
        return datetime.now().strftime("%Y-%m-%d")
    
    def get_day(self):
        """Returns the current day of the week."""
        return datetime.now().strftime("%A")
        
dt_info = DateTimeInfo()
print("Time:", dt_info.get_time())
print("Date:", dt_info.get_date())
print("Day:", dt_info.get_day())




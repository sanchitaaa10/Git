from datetime  import datetime

class Time:
  def get_date(self):
     """Returns the current date in YYYY-MM-DD format."""
     return datetime.now().strftime("%Y-%m-%d")
    
def get_time(self):
        """Returns the current time in HH:MM:SS format."""
        return datetime.now().strftime("%H:%M:%S")



dt_info = Time()
print("Date:", dt_info.get_date())
print("Time:", dt_info.get_time())


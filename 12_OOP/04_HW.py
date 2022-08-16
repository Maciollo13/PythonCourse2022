import time
import datetime
import pytz


class Watch:
    def __init__(self, name, time_zone):
        self.time_zone = time_zone
        self.name = name
        self.time = datetime.datetime.now()

    def show_time(self):
        zone = pytz.timezone(self.time_zone)
        time_in_zone = datetime.datetime.now(zone)
        current_time = time_in_zone.strftime("%H:%M:%S")
        print(f"In {self.time_zone} time zone is {current_time}")


class Calendar:

    def show_date(self):
        date = datetime.datetime.now()
        print(f"{date.day}:{date.month}:{date.day}")

def show_zones():
    return pytz.all_timezones


hublot = Watch("Hublot","America/New_York")
hublot.show_time()
#print(show_zones())

class Time:
    def __init__(self, hours, minutes, seconds, ms):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.ms = ms

    def get_time(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}.{self.ms}"

championship = Championship()

grand_prix1 = championship.define_grand_prix("Ali Grand Prix")
driver1 = championship.create_driver("Ali")

time = championship.set_time(grand_prix1, driver1, 1, 32, 45, 500)
if time is not None:
    print(f"Time set: {time.get_time()}")
else:
    print("Failed to set time")

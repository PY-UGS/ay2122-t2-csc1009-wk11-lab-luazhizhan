class ClockTime:
    """
    ClockTime class that takes and print hours, mintutes and seconds\n

    Methods

    1. setHours
    2. setMinutes
    3. setSeconds
    4. setTime
    5. showTime
    """

    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def setHours(self, hours):
        if hours < 0 or hours > 24:
            raise ValueError("Hours must be between 0 to 24")
        self.hours = hours

    def setMinutes(self, minutes):
        if minutes < 0 or minutes > 59:
            raise ValueError("Minutes must be between 0 to 59")
        self.minutes = minutes

    def setSeconds(self, seconds):
        if seconds < 0 or seconds > 59:
            raise ValueError("Seconds must be between 0 to 59")
        self.seconds = seconds

    def setTime(self, hours, minutes, seconds):
        self.setHours(hours)
        self.setMinutes(minutes)
        self.setSeconds(seconds)

    def showTime(self):
        """
        return <hours>:<minutes>:<seconds>
        """
        return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)


def main():
    try:
        # Get hour, minutes and seconds from user
        hours = int(input("Enter hours: "))
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter minutes: "))

        # Instantiate ClockTime object
        clockTime = ClockTime()

        # Set hours, minutes and, seconds
        clockTime.setHours(hours)
        clockTime.setMinutes(minutes)
        clockTime.setSeconds(seconds)

        # Print time
        print("\nTime : " + clockTime.showTime())

    except ValueError as e:
        print(str(e)+"\n")
        main()


main()

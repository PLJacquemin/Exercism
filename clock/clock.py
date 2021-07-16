class Clock:
    def __init__(self, hour, minute):
        self.minute = minute + hour*60

    def __repr__(self):
        return "%02d:%02d"%((self.minute//60)%24,self.minute%60)

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __add__(self, minutes):
        self.minute += minutes
        return self

    def __sub__(self, minutes):
        self.minute -= minutes
        return self

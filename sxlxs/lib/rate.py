class Rate:
    def __init__(self, location, room_type, credits):
        self.location = location
        self.room_type = room_type
        self.credits = credits

    def print_rate(self):
        print("The room " + self.room_type + " located in " + self.location + " costs " + self.credits + " credits.")

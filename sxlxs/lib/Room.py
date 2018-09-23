class Room:
    def __init__(self, name, location, room_type, rate, description, issues):
        self.name = name
        self.location = location
        self.room_type = room_type
        self.rate = rate
        self.description = description
        self.issues = issues

    def print_room(self):
        print("The room " + self.name + " located in " + self.location + " is a " + self.room_type + " that " + self.description + " and has " + len(issues) + " issues.")

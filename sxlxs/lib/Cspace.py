from .prompt import select_calender_prompt
from .Client import Client
from .Room import Room
# from .Calenders import Calenders

class Cspace:
    def __init__(self, workbook):
        self.workbook = workbook
        self.clients = self.get_clients()
        self.rooms = self.get_rooms()
        
    # function that extracts clients from client excel sheet and returns them in a list
    def get_clients(self):
        client_sheet = self.workbook['Clients']
        clients = []


        return clients

    def get_rooms(self):
        rooms = []
        starting_row = 2
        facility_sheet = self.workbook['Facilities']
        rate_sheet = self.workbook['Rates']

        # function to get the rate of the room by matching location and room_type
        def get_rate(location, room_type):
            for row in range(starting_row, rate_sheet.max_row):
                row_number = str(row)
                if(location is rate_sheet['A'+row_number].value and room_type is rate_sheet['B'+row_number].value):
                    return rate_sheet['C'+row_number].value

        # loop through the rows in the facility sheet and combine with rate sheet
        for row in range(starting_row, facility_sheet.max_row):
            row_number = str(row)
            name = facility_sheet['A'+row_number].value
            room_type, location = (facility_sheet['B'+row_number].value, facility_sheet['C'+row_number].value)
            description = facility_sheet['D'+row_number].value
            issues = facility_sheet['E'+row_number].value
            rate = get_rate(location, room_type)
            rooms.append(Room(name, location, room_type, rate, description, issues))

        return rooms

    def get_calenders(self):
        pass

    def get_calender_months(self):
        selected_months = []
        for sheet in self.workbook.sheetnames:
            if sheet not in ["Clients", "Facilities", "Rates"]:
                selected_months.append(sheet)
            else:
                None
        selected_months = select_calender_prompt(selected_months)
        return selected_months


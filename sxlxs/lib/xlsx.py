from .client import Client
from .room import Room
from .rate import Rate

# function that extracts clients from client excel sheet and returns them in a list
def get_clients(client_sheet):
    name_list = []
    for row in client_sheet.iter_rows('A{}:A{}'.format(client_sheet.min_row, client_sheet.max_row)):
        for cell in row:
            name_list.append(cell.value)

    # get rid of column title
    del name_list[0]

    # create a list that stores all the client dicts
    client_list = []
    for clients in name_list:
        first_name = clients.split()[0]
        last_name = clients.split()[1]

        client_list.append(Client(first_name, last_name, "none", "none"))
    return client_list

def get_rates(rate_sheet):
    pass

def get_rooms(room_sheet):
    pass

def get_calenders():
    pass

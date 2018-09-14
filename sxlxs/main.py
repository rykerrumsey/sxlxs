import os
import requests
import json

from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal
from .core.exc import mainError
from cement.utils import fs
from .controllers.base import Base
from openpyxl import Workbook, load_workbook
from jinja2 import Template, FileSystemLoader, Environment

# configuration defaults
CONFIG = init_defaults('sxlxs')

class Sxlxs(App):
    """sxlxs primary application."""

    class Meta:
        label = 'sxlxs'

        # configuration defaults
        config_defaults = CONFIG

        # call sys.exit() on close
        close_on_exit = True

        # load additional framework extensions
        extensions = [
            'yaml',
            'colorlog',
            'jinja2',
        ]

        # configuration handler
        config_handler = 'yaml'

        # configuration file suffix
        config_file_suffix = '.yml'

        # set the log handler
        log_handler = 'colorlog'

        # set the output handler
        output_handler = 'jinja2'
      
        # register handlers
        handlers = [
            Base
        ]
        
    templateLoader = FileSystemLoader('./templates')
    templateEnv = Environment(loader=templateLoader)
    TEMPLATE_FILE = "main_template.html"
        
    if os.path.exists('./data/bookings.xlsx'):
        print("Bookings exists")
    else:
        print("Bookings does not exist")

    wb = load_workbook("./data/bookings.xlsx")
    client_sheet = wb["Clients"]
    print(client_sheet)
    template = templateEnv.get_template(TEMPLATE_FILE)

    print(wb.sheetnames)
    
    def get_profiles():
        #temporary because we can get the amount 
        amount = 20

        r = requests.get('https://randomuser.me/api/?exc=login,gender,name,email,registered,id,nat&results=' + str(amount)  + '&seed=abc')

        #must parse json before accessing the object
        json_data = json.loads(r.text)

        #clean up object before sending out
        results = json_data['results']
        print(results) 
        return results

    def get_clients(client_sheet):
        name_list = []
        for row in client_sheet.iter_rows('A{}:A{}'.format(client_sheet.min_row, client_sheet.max_row)):
            for cell in row:
                name_list.append(cell.value)
        
        #get rid of column title
        del name_list[0]
        
        client_list = []
    
        print(name_list)
        
        for clients in name_list:
            first_name = clients.split()[0]
            last_name = clients.split()[1]
            
            print(first_name)
            print(last_name)
            
            current_client = {}
            current_client["first"] = first_name
            current_client["last"] = last_name

            client_list.append(current_client)
            
        print(client_list)

        return client_list
    client_data = get_clients(client_sheet)
    
    
    def extract_pictures(profiles):
        pictures = []
        
        print(profiles)

        for client in profiles:
            print("-------------")
            print(client['picture']['large'])
            print("-------------")
            pictures.append(client['picture']['large'])

        print(pictures)
        return pictures

    output = template.render(workbook=wb.sheetnames, clients=client_data, number_of_worksheets=len(wb.sheetnames), number_of_clients=len(client_data), pictures=extract_pictures(get_profiles()))

    # create the index.html file if it doesn't exist and write the rendered template to it
    html_file = open("./data/index.html", 'w')
    html_file.write(output)
    html_file.close()

def main():
    with Sxlxs() as app:
        try:
            app.run()

        except AssertionError as e:
            print('AssertionError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except mainError:
            print('mainError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('\n%s' % e)
            app.exit_code = 0


if __name__ == '__main__':
    main()

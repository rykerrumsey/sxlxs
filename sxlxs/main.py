import os

from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal
from .core.exc import mainError
from cement.utils import fs

# controllers
from .controllers.base import Base
from .controllers.generate import Generate

from openpyxl import Workbook, load_workbook
from jinja2 import Template, FileSystemLoader, Environment
from pyfiglet import Figlet

# user defined modules
from .lib.xlsx import *
from .lib.prompt import *

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
            Base,
            Generate
        ]

        hooks = []

    # print title screen
    # tested 'isometric3' 'o8' 'jazmine' 
    print()
    f = Figlet(font='cosmic')
    print(f.renderText('sxlxs'))

    # load templates into program
    templateLoader = FileSystemLoader('./templates')
    templateEnv = Environment(loader=templateLoader)
    TEMPLATE_FILE = "main_template.html"

    wb = load_workbook("./data/bookings.xlsx")
    template = templateEnv.get_template(TEMPLATE_FILE)

    client_data = get_clients(wb['Clients'])
    rate_data = get_rates(wb['Rates'])
    room_data = get_rooms(wb['Facilities'])
    #calender_data = get_calenders()

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
    asyncio.run(main())

import os

from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal
from .core.exc import mainError
from cement.utils import fs

from openpyxl import load_workbook

# controllers
from .controllers.base import Base
from .controllers.generate import Generate

# user defined modules
from .lib.Cspace import Cspace
from .lib.utils import printTitleScreen

import json

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

    printTitleScreen()

    cspace = Cspace(load_workbook("./data/bookings.xlsx"))
    rooms = cspace.get_rooms()

    """
    if App.pargs.json:
        render_json(cspace)
    elif App.pargs.html:
        render_html(cspace)
    else:
        pass
    """

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

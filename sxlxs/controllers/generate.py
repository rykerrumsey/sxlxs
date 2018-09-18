from pathlib import Path
from cement import Controller, ex
from cement.utils import fs
from ..lib.prompt import *

class Generate(Controller):
    class Meta:
        label = 'generate'
        stacked_type = 'embedded'
        stacked_on = 'base'

    @ex(
        help='generate html from spreadsheet',
        arguments=[
            ( ['file_path'],
              {'help': 'sxlxs generate-html file_path',
               'action': 'store'} )
        ]
    )
    # generate html from excel file
    # todo: move to lib dir
    def generate_html(self):
        calenders = ['July-2018', 'August-2018', 'September-2018']
        file_path = self.app.pargs.file_path
        if verify_file(file_path):
            self.app.log.info('Parsing spreadsheet %s' % file_path)
            show_calender_prompt(calenders)
        else:
            self.app.log.error('%s does not exist' % file_path)

    @ex(help='generate json from spreadsheet')
    def generate_json(self):
        pass

# verify to make sure the file exists return True if it does False if it does not
# todo: move to lib dir
def verify_file(file_path):
    # expand file path
    file_path = fs.abspath(file_path)

    # convert file_path to Path object
    file_path = Path(file_path)

    # check to see if the file exist
    if file_path.is_file():
        return True
    else:
        return False

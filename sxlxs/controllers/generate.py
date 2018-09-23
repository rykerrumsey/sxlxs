from cement import Controller, ex
from cement.utils import fs

class Generate(Controller):
    class Meta:
        label = 'generate'
        stacked_type = 'embedded'
        stacked_on = 'base'

    @ex(
        help='generate html or json from spreadsheet',
        arguments=[
            ( ['--html'],
              {'help': 'sxlxs generate --html file_path',
               'action': 'store'} ),

            ( ['--json'],
              {'help': 'sxlxs generate --json file_path',
             'action': 'store'} )
        ]
    )
    def generate(self):
        if self.app.pargs.html:
            self.app.log.info('Generating HTML...')
        if self.app.pargs.json:
            self.app.log.info('Generating JSON...')


from jinja2 import Template, FileSystemLoader, Environment
from utils import verify_file

def generate_html():
    calenders = ['July-2018', 'August-2018', 'September-2018']
    file_path = self.app.pargs.file_path
    if verify_file(file_path):
        self.app.log.info('Parsing spreadsheet %s' % file_path)
        show_calender_prompt(calenders)
    else:
        self.app.log.error('%s does not exist' % file_path)


def message():
    print("Exported to html successfully!")

    # load templates into program
    templateLoader = FileSystemLoader('./templates')
    templateEnv = Environment(loader=templateLoader)
    TEMPLATE_FILE = "main_template.html"

    template = templateEnv.get_template(TEMPLATE_FILE)

    # generate the final html file by taking the template and inserting the data
    output = template.render(workbook=wb.sheetnames, clients=client_data, number_of_worksheets=len(wb.sheetnames), number_of_clients=len(client_data))

    # create the index.html file if it doesn't exist and write the rendered template to it
    html_file = open("./data/index.html", 'w')
    html_file.write(output)
    html_file.close()
"""
    print("------------------------------------------------")
    print("/data/index.html has been generated succesfully!")
    print("------------------------------------------------")
"""

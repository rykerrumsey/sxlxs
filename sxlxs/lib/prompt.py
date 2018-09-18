import inquirer
from pprint import pprint

def show_calender_prompt(calenders):
    questions = [
        inquirer.Checkbox('calenders',
                          message="Please select the calenders you would like to import",
                          choices=calenders
                          )
    ]

    answers = inquirer.prompt(questions)

    pprint(answers)


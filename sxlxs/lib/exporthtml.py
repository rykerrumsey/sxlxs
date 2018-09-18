def message():
    print("Exported to html successfully!")


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

    message()

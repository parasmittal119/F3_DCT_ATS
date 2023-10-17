import os

from reportlab.pdfgen import canvas

import gui_global

page1 = f"{gui_global.image_directory_location}report_format_page.jpg"


#  customer_name = 'NA', part_number = "NA", serial_number = "NA", config_version = "NA",
#                    mac_id = "NA", operator = "NA", date = "NA",


def generateReport(c, parameters=[], final_result="NA"):
    # basic drawing of the report template
    c.drawImage(page1, 20, 20, 550, 800)
    x = 175
    y = 690
    basic_parameters = []
    for i in range(6):
        basic_parameters.append(parameters[i])
    for i in range(len(basic_parameters)):
        c.drawString(x, y, basic_parameters[i].upper())
        y = y - 16

    c.drawString(x, 594, str(parameters[6].upper()) + " " + str(parameters[7].upper()))

    x = 440
    y = 545
    test_parameter = []
    for i in range(8, 33):
        test_parameter.append(parameters[i])

    for i in range(len(test_parameter)):
        c.drawString(x, y, test_parameter[i])
        y = y - 15

    c.setFont(size=12, psfontname="Helvetica")
    c.drawString(115, 150, parameters[-1])


def Creation(parameters: list):
    fileName = str(parameters[1])+"#"+str(parameters[2])+"_"+str(parameters[-1])+".pdf"
    fileName = os.path.join(gui_global.directory_location+"reports", fileName)
    ARR = os.listdir(f"{gui_global.directory_location}reports/")
    if fileName[11:] in ARR:
        pass
    else:
        c = canvas.Canvas(fileName)
        generateReport(c, parameters=parameters)
        c.showPage()
        c.save()
    # print(parameters)

#TEST CASE
# Creation(parameters=["ui","ui","ui","ui","ui","ui","ui","ui","ui","ui","ui","ui","ui","ui","ui","ui","ui","ui","ui","ui","ui","ui","ui","ui","ui","ui","ui","ui","ui","ui","ui","ui","ui",])
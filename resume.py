# PDF Resume Creator
# 	- Create a python program that will create your personal resume in PDF format
# 	- All personal details are stored in a JSON file
# 	- Your program should read the JSON file and write the details in the PDF
# 	- The output file should be: LASTNAME_FIRSTNAME.pdf

import json
from fpdf import FPDF

with open('resume_info.json') as json_file:
    dataResume = json.load(json_file)




# P. S: these notes are from the yt vid (https://www.youtube.com/watch?v=q70xzDG6nls) i watched
# create FPDF object
# layout ("P", "L")
# unit ("mm", "cm", "in")
# format ("A3", "A4", (default), "A5", "Letter", "Legal", (100, 150) -> first integer = width, second integer = height)

resumepdf = FPDF('P', 'mm', 'Letter')

# add page
resumepdf.add_page()

# specify font 
# fonts can be times, courier, helvetica, symbol, zpfdingbats
# 'B' (bold), 'U' (underline), 'I' (italic), '' (regular), combination ('BU')
resumepdf.set_font('times', '', 14)

# adding text
# w = width
# h = height
# txt = text
# ln = (0 - False, 1 - True = move cursor down to next line)
# border (0 - False, 1 - True = add border around cell)
resumepdf.cell(40, 10, "Hello World!", ln=True)
resumepdf.cell(80, 10, "Goodbye World!")

resumepdf.output("CANDO_IRISH MICOLE.pdf")
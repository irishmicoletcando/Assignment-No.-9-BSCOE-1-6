# PDF Resume Creator
# 	- Create a python program that will create your personal resume in PDF format
# 	- All personal details are stored in a JSON file
# 	- Your program should read the JSON file and write the details in the PDF
# 	- The output file should be: LASTNAME_FIRSTNAME.pdf

import json
from fpdf import FPDF

with open('resume_info.json') as json_file:
    dataResume = json.load(json_file)

name = dataResume["name"]
address = dataResume["address"]
phone = dataResume["phone"]
email = dataResume["email"]
github = dataResume["github"]
website = dataResume["website"]
careerObjectives = dataResume["careerObjectives"]
skill1 = dataResume["skill1"]
skill2 = dataResume["skill2"]
skill3 = dataResume["skill3"]
skill4 = dataResume["skill4"]
skill5 = dataResume["skill5"]
university = dataResume["university"]
course = dataResume["course"]
yearUniversity = dataResume["yearUniversity"]
seniorhighschool = dataResume["seniorhighschool"]
yearSeniorhighschool = dataResume["yearSeniorhighschool"]
seniorHighschoolText = dataResume["seniorHighschoolText"]
highschool = dataResume["highschool"]
highschoolText = dataResume["highschoolText"]
yearHighschool = dataResume["yearHighschool"]
certification1 = dataResume["certification1"]
yearCertification1 = dataResume["yearCertification1"]
issuerCertification1 = dataResume["issuerCertification1"]
certification2 = dataResume["certification2"]
yearCertification2 = dataResume["yearCertification2"]
issuerCertification2 = dataResume["issuerCertification2"]
award1 = dataResume["award1"]
yearAward1 = dataResume["yearAward1"]
detailsAward1 = dataResume["detailsAward1"]
award2 = dataResume["award2"]
yearAward2 = dataResume["yearAward2"]
detailsAward2 = dataResume["detailsAward2"]
award3 = dataResume["award3"]
yearAward3 = dataResume["yearAward3"]
detailsAward3 = dataResume["detailsAward3"]

# P. S: these notes are from the yt vid (https://www.youtube.com/watch?v=q70xzDG6nls)
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
resumepdf.set_font('times', 'B', 16)
resumepdf.set_margins(top=20, left=20, right=20)
# adding text
# w = width
# h = height
# txt = text
# ln = (0 - False, 1 - True = move cursor down to next line)
resumepdf.cell(0, 0, name,  align='C', ln=True)
resumepdf.set_font('times', '', 13)
resumepdf.cell(0, 12, address + " | " + phone + " | " + email,  align='C', ln=True)
resumepdf.cell(0, 0, github + " | " + website,  align='C', ln=True)
resumepdf.cell(0, 7, " ", align='L', ln=True)

resumepdf.set_font('times', 'B', 14)
resumepdf.cell(0, 10, "CAREER OBJECTIVES", align='L', ln=True)
resumepdf.set_font('times', '', 13)
resumepdf.cell(0, 2, careerObjectives, align='L', ln=True)

resumepdf.cell(0, 7, " ", align='L', ln=True)
resumepdf.set_font('times', 'B', 14)
resumepdf.cell(0, 6, "SKILLS", align='L', ln=True)
resumepdf.set_font('times', '', 13)
resumepdf.cell(0, 5, skill1, align='L', ln=True)
resumepdf.cell(0, 5, skill2, align='L', ln=True)
resumepdf.cell(0, 5, skill3, align='L', ln=True)
resumepdf.cell(0, 5, skill4, align='L', ln=True)
resumepdf.cell(0, 5, skill5, align='L', ln=True)

resumepdf.cell(0, 7, " ", align='L', ln=True)
resumepdf.set_font('times', 'B', 14)
resumepdf.cell(0, 6, "EDUCATION", align='L', ln=True)
resumepdf.set_font('times', 'B', 13)
resumepdf.cell(0, 5, university, align='L', ln=False)
resumepdf.cell(0, 5, yearUniversity, align='R', ln=True)
resumepdf.set_font('times', 'I', 13)
resumepdf.cell(0, 5, course, align='L', ln=True)
resumepdf.cell(0, 5, " ", align='L', ln=True)
resumepdf.set_font('times', 'B', 13)
resumepdf.cell(0, 5, seniorhighschool, align='L', ln=False)
resumepdf.cell(0, 5, yearSeniorhighschool, align='R', ln=True)
resumepdf.set_font('times', 'I', 13)
resumepdf.cell(0, 5, seniorHighschoolText, align='L', ln=True)
resumepdf.cell(0, 5, " ", align='L', ln=True)
resumepdf.set_font('times', 'B', 13)
resumepdf.cell(0, 5, highschool, align='L', ln=False)
resumepdf.cell(0, 5, yearHighschool, align='R', ln=True)
resumepdf.set_font('times', 'I', 13)
resumepdf.cell(0, 5, highschoolText, align='L', ln=True)

resumepdf.cell(0, 7, " ", align='L', ln=True)
resumepdf.set_font('times', 'B', 14)
resumepdf.cell(0, 6, "CERTIFICATIONS", align='L', ln=True)
resumepdf.set_font('times', 'B', 13)
resumepdf.cell(0, 5, certification1, align='L', ln=False)
resumepdf.cell(0, 5, yearCertification1, align='R', ln=True)
resumepdf.set_font('times', 'I', 13)
resumepdf.cell(0, 5, issuerCertification1, align='L', ln=True)
resumepdf.cell(0, 5, " ", align='L', ln=True)
resumepdf.set_font('times', 'B', 13)
resumepdf.cell(0, 5, certification2, align='L', ln=False)
resumepdf.cell(0, 5, yearCertification2, align='R', ln=True)
resumepdf.set_font('times', 'I', 13)
resumepdf.cell(0, 5, issuerCertification2, align='L', ln=True)

resumepdf.cell(0, 7, " ", align='L', ln=True)
resumepdf.set_font('times', 'B', 14)
resumepdf.cell(0, 6, "AWARDS", align='L', ln=True)
resumepdf.set_font('times', 'B', 13)
resumepdf.cell(0, 5, award1, align='L', ln=False)
resumepdf.cell(0, 5, yearAward1, align='R', ln=True)
resumepdf.set_font('times', 'I', 13)
resumepdf.cell(0, 5, detailsAward1, align='L', ln=True)
resumepdf.cell(0, 5, " ", align='L', ln=True)
resumepdf.set_font('times', 'B', 13)
resumepdf.cell(0, 5, award2, align='L', ln=False)
resumepdf.cell(0, 5, yearAward2, align='R', ln=True)
resumepdf.set_font('times', 'I', 13)
resumepdf.cell(0, 5, detailsAward2, align='L', ln=True)
resumepdf.cell(0, 5, " ", align='L', ln=True)
resumepdf.set_font('times', 'B', 13)
resumepdf.cell(0, 5, award3, align='L', ln=False)
resumepdf.cell(0, 5, yearAward3, align='R', ln=True)
resumepdf.set_font('times', 'I', 13)
resumepdf.cell(0, 5, detailsAward3, align='L', ln=True)

resumepdf.output("CANDO_IRISH MICOLE.pdf")
from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
inpu = PdfFileReader(open("dst.pdf", "rb"))

# print how many pages inpu has:
# print("documen.pdf has %d pages." % inpu.getNumPages())

page_text = inpu.getPage(24).extractText()
page = inpu.getPage(24)

# for content in page:   # print(dir(content))   # print(content)
# print(dir(page))

hr_categories = {
"Structural Movement",
"Dampness, rot and infestation",
"Chimney stacks",
"Roofing including roof space",
"Rainwater fittings",
"Main walls",
"Windows, external doors and joinery",
"External decorations",
"Conservatories / porches"
"Communal areas",
"Garages and permanent outbuildings",
"Outside areas and boundaries"
"Ceilings",
"Internal walls",
"Floors including sub-floors",
"Internal joinery and kitchen fittings",
"Chimney breasts and fireplaces",
"Internal decorations",
"Cellars",
"Electricity",
"Gas",
"Water, plumbing and bathroom fittings",
"Heating and hot water",
"Drainage"
}

for text in page_text:
    if text

print(page_text)


# if "Structural Movement" in page_text:
#     print(page_text.split("\n"))

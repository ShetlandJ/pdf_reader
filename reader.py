from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
input1 = PdfFileReader(open("dst.pdf", "rb"))

page_text = input1.getPage(24).extractText()
page = input1.getPage(24)

hr_categories = {
"Structural Movement": "",
"Dampness, rot and infestation": "",
"Chimney stacks": "",
"Roofing including roof space": "",
"Rainwater fittings": "",
"Main walls": "",
"Windows, external doors and joinery": "",
"External decorations": "",
"Conservatories / porches"
"Communal areas": "",
"Garages and permanent outbuildings": "",
"Outside areas and boundaries"
"Ceilings": "",
"Internal walls": "",
"Floors including sub-floors": "",
"Internal joinery and kitchen fittings": "",
"Chimney breasts and fireplaces": "",
"Internal decorations": "",
"Cellars": "",
"Electricity": "",
"Gas": "",
"Water, plumbing and bathroom fittings": "",
"Heating and hot water": "",
"Drainage": ""
}

hr_titles = [
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
]

#
# for text in page_text:
#     if text
#
# print(page_text)


def get_data_array():
    phrase = " \nStructural Movement"

    if phrase in page_text:
        text_array = page_text.split("\n \n")
        index = text_array.index(phrase)
        final_text_array = text_array[index:]

        remember = final_text_array.index(' \n  \nRemember')

        # print(remember)
        print(final_text_array)

        super_final_array = final_text_array[:remember]

        arr = []

        for el in super_final_array:
            print(el)
            if el == "1" or el == "2" or el == "3" or el == "-" or el == "-":
                arr.append(el)
            # elif len(el) < 2:
            #     arr.append(el)


        # print(arr)
        # print(len(arr))
        # print(len(hr_titles))
        # print(list(zip(hr_titles, arr)))

get_data_array()

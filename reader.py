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
#
# for text in page_text:
#     if text
#
# print(page_text)


def get_data_array():
    phrase = "Structural Movement"

    if phrase in page_text:
        text_array = page_text.split("\n \n")
        print(text_array)

        arr = []

        # print(final_text_array)

        for el in text_array:
            if el == "1" or el == "2" or el == "3" or el == "-" or el == "-":
                arr.append(el)

        print(len(arr))
        print(len(hr_categories))

                # for el in final_text_array:
                #     if el == " " or el == "  " or el == "",:
                #         final_text_array.remove(el)
                #
                # del final_text_array[-1]
                # # return final_text_array
                # print(arr)
                # print(len(arr))
                # print(len(hr_categories))
                # zipped = zip(hr_categories, arr)
                # print(list(zipped))
                # counter = 0
                # for num in arr:




                    # def build_object():
                    #     text_array = get_data_array()
                    #
                    #     for counter, value in enumerate(text_array):
                    #         print(counter, value)

                    # print(text_array)

get_data_array()

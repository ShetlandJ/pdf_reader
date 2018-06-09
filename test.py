import PyPDF2


input1 = PyPDF2.PdfFileReader(open("dst.pdf", "rb"))

page = input1.getPage(24)
page_text = page.extractText()


start = page_text.index("Structural Movement")
end = page_text.index("Remember")

text = page_text[start:end]  # trim down what's needed


making_col_name = True
lines = text.split("\n")
data = []
col_name = ""

for l in lines:
    l = l.strip()
    if making_col_name:
        if l:
            col_name += l
        else:
            # end of name, should be a newline between name and the value
            making_col_name = False
    else:
        if l:  # must be the value, since nothing else on 'non name lines'
            try:
                data.append((col_name, int(l)))
            except (ValueError, TypeError):
                data.append((col_name, "0"))
            col_name = ""
        else:  # empty line before next name
            making_col_name = True


for t in data:
    print(t[0], t[1])

from PyPDF2 import PdfWriter

merger=PdfWriter()

pdfs=[]
n=int(input("how many you want to merge ?\n"))

for i in range(0,n):
    name=input(f"Enter the name of  pdf no {i+1} :")
    pdfs.append(name)

try:
    for pdf in pdfs:
        merger.append(pdf)
except Exception as e:
    print(e)

merger.write("merged-pdf.pdf")
merger.close()

    
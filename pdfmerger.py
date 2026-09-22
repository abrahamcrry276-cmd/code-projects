#python pdfmerger.py new_file_name(don't add .pdf) [add as many pdfs as u want]
import pypdf
import sys

new_file_name = sys.argv[1]
inputs = sys.argv[2:]

def pdf_combiner(pdf_list):
    writer = pypdf.PdfWriter()
    for pdf in pdf_list:
        writer.append(pdf)
    with open(f'{new_file_name}.pdf', 'wb') as new_file:
        writer.write(new_file)
pdf_combiner(inputs)


###this makes the pdf rotated(-90), that's how you got tilt.pdf
# with open('dummy.pdf', 'rb') as file:
#     reader = pypdf.PdfReader(file)
#     page = reader.get_page(0)
#     page.rotate(-90)
#     writer = pypdf.PdfWriter()
#     writer.add_page(page)
#     with open('tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)
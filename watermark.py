#python watermark.py pdf

import pypdf
import sys

pdf = sys.argv[1]

reader = pypdf.PdfReader(pdf)
pages = reader.pages

wtrmark = pypdf.PdfReader('wtr.pdf')
watermark = wtrmark.pages[0]

writer = pypdf.PdfWriter()
for item in pages:
    item.merge_page(watermark, False,True)
    writer.add_page(item)

with open(f'W{pdf}', 'wb') as new_file:
    writer.write(new_file)
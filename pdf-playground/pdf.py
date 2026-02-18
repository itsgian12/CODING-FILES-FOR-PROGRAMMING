from pypdf import PdfWriter
import sys

def pdf_combiner(pdf_list):
    writer = PdfWriter()

    for pdf in pdf_list:
        writer.append(pdf)

    with open("super.pdf", "wb") as f:
        writer.write(f)

pdf_combiner(sys.argv[1:])




"""this is no longer working since pypdf updated to version 6.7.1, the code is now above"""
# import pypdf
# import sys

# inputs = sys.argv[1:]

# def pdf_combiner(pdf_list):
#     merger = pypdf.PdfMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write("super.pdf")
#     merger.close()

# pdf_combiner(inputs)

""" this is for tilt.pdf """
# with open("dummy.pdf", "rb") as file:
#     reader = pypdf.PdfReader(file)
#     page = reader.pages[0]
#     page.rotate(90)
#     writer = pypdf.PdfWriter()
#     writer.add_page(page)
#     with open("tilt.pdf", "wb") as new_file:
#         writer.write(new_file)
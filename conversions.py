import os
import shutil
from pdf2image import convert_from_path
import docx2pdf
from docx2pdf import convert


def remove_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        os.remove(file_path)


# def text_to_pdf(documents_to_convert):
#         for filename in os.listdir(documents_to_convert):
#             if filename.endswith('.docx'):
#                 pdf_filename = f"{filename[:-5]}.pdf"
#                 converting_path = os.path.join(documents_to_convert, pdf_filename)
#                 print(f"this is the converting path: {converting_path}")
#                 convert(converting_path)
#                 print(f"Converted {filename}")
#         # remove_files_in_folder(documents_to_convert)


def convert_to_images(input_pdf_documents, output_image_documents):
    remove_files_in_folder(output_image_documents)
    for filename in os.listdir(input_pdf_documents):
        pdf_path = os.path.join(input_pdf_documents, filename)
        images = convert_from_path(pdf_path)
        for i, image in enumerate(images):
            image_filename = f"{filename[:-4]}_{i+1}.png"
            image_path = os.path.join(output_image_documents, image_filename)
            image.save(image_path, 'PNG')
        print(f"converted {filename} to images")
      

# text_to_pdf('/Users/ryanasermely/Desktop/podcom/store', '/Users/ryanasermely/Desktop/podcom/store')
# convert_to_images('/Users/ryanasermely/Desktop/podcom/store', '/Users/ryanasermely/Desktop/podcom/image_store')
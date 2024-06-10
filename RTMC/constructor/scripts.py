import os, csv, io

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from pdfrw import PdfReader, PdfWriter, PageMerge

from django.conf import settings
from django.contrib.staticfiles import finders

from .models import Template, Participant


def split_csv(csv_file) -> list:
    
    content = csv_file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(content)
    
    rows = []
    
    for row in reader:

        rows.append([row['fullname'], row.get('organization_name', None)])
    
    return rows




def find_fileds_coordinates(pdf_path) -> list:
    
    pdf = PdfReader(pdf_path)
    
    for page in pdf.pages:
        
        annotations = page['/Annots']
        
        if annotations:
            
            coordinates = [None, None]
            
            for annotation in annotations:
                
                if annotation['/T'] and annotation['/T'][1:-1] == 'fullname':
                    
                    rect = annotation['/Rect']
                    
                    x1, y1, x2, y2 = rect
                    
                    coordinates[0] = [float(x1), float(y1), float(x2) - float(x1), float(y2) - float(y1)]
                    
                    continue
                
                if annotation['/T'] and annotation['/T'][1:-1] == 'organization_name':
                    
                    rect = annotation['/Rect']
                    
                    x1, y1, x2, y2 = rect
                    
                    coordinates[1] = (float(x1), float(y1), float(x2) - float(x1), float(y2) - float(y1))
                    
        return coordinates
    
    return None




def create_overlay(data_dict: dict, template: Template):
    
    packet = io.BytesIO()
    
    can = canvas.Canvas(packet, pagesize=letter)
    
    pdfmetrics.registerFont(TTFont('Tahoma Bold', finders.find('fonts/tahoma.ttf')))
    
    
    font_size = 25
     
    can.setFont("Tahoma Bold", font_size)
    
    text_width = can.stringWidth(data_dict['fullname'], "Tahoma Bold", font_size)
    
    
    while text_width > template.fullname_textbox_width and font_size > 6:
        
        font_size -= 1
        
        can.setFont("Tahoma Bold", font_size)
        
        text_width = can.stringWidth(data_dict['fullname'], "Tahoma Bold", font_size)
    
    
    fullname_x = template.fullname_x_coordinate + (template.fullname_textbox_width - text_width) / 2
    fullname_y = template.fullname_y_coordinate + (template.fullname_textbox_height - font_size) / 2
    
    can.drawString(fullname_x, fullname_y, data_dict['fullname'])
    
    
    if template.doc_type == 'w' and data_dict['organization_name'] != None:
        
        font_size = 25
        
        can.setFont("Tahoma Bold", font_size)
        
        text_width = can.stringWidth(data_dict['organization_name'], "Tahoma Bold", font_size)
        
        
        while text_width > template.organization_textbox_width  and font_size > 4:
        
            font_size -= 1
        
            can.setFont("Tahoma Bold", font_size)
            
            text_width = can.stringWidth(data_dict['organization_name'], "Tahoma Bold", font_size)
        
        
        organization_x = template.organization_x_coordinate + (template.organization_textbox_width - text_width) / 2
        organization_y = template.organization_y_coordinate + (template.organization_textbox_height - font_size) / 2
        
        can.drawString(organization_x, organization_y, data_dict['organization_name'])
    
     
    can.save()
    
    packet.seek(0)
    
    return packet


def delete_annotations(pdf: PdfReader) -> PdfReader:
    
    for page in pdf.pages:

        if page['/Annots']:
            
            del page['/Annots']
            
    return pdf


def construct(template: Template, participant: Participant) -> str:

    pdf = PdfReader(template.path_to_file)
    
    data_dict = {
        'fullname': participant.fullname,
    }
    
    if template.doc_type == 'w':
        
        data_dict.update({'organization_name': participant.organization_name})


    overlay_pdf = PdfReader(create_overlay(data_dict, template))
    
    for page_num, page in enumerate(pdf.pages):
        
        PageMerge(page).add(overlay_pdf.pages[page_num]).render()


    pdf = delete_annotations(pdf)
    
    
    full_save_path = os.path.join(settings.MEDIA_ROOT, 'constructor', 'documents', template.name + '_' + participant.fullname + '.pdf')
    
    PdfWriter(full_save_path, trailer=pdf).write()
    
    return full_save_path

import os

from fillpdf import fillpdfs

from django.conf import settings

from.models import Template, Participant


import csv


def split_csv(csv_file) -> list:
    
    content = csv_file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(content)
    
    rows = []
    
    for row in reader:
        print(row)
        rows.append([row['fullname'], row.get('organization_name', None)])
    
    return rows


def construct(template: Template, participant: Participant):
    
    pdf_path = template.path_to_file

    full_save_path = os.path.join(settings.MEDIA_ROOT, 'constructor', 'documents', template.name + '_filles.pdf')
    flatt = os.path.join(settings.MEDIA_ROOT, 'constructor', 'documents', template.name + '_flatted.pdf')

    fillpdfs.get_form_fields(pdf_path)

    if template.doc_type == 'wo':

        data_dict = {
            'fullname': participant.fullname,
        }
        
    else:
        
        data_dict = {
            'fullname': participant.fullname,
            'organization_name': participant.organization_name,
        }

    fillpdfs.write_fillable_pdf(pdf_path, full_save_path, data_dict)

    # If you want it flattened:
    fillpdfs.flatten_pdf(full_save_path, flatt)
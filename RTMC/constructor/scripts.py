from fillpdf import fillpdfs

import csv


def split_csv(csv_file) -> list:
    
    content = csv_file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(content)
    
    rows = []
    
    for row in reader:
        
        rows.append([row['fullname'], row.get('organization_name', None)])
    
    return rows


def script():
    pdf_path = '.\\documents\\сертификат.pdf'
    output_pdf_path = '.\\documents\\new_сертификат.pdf'
    flatt = '.\\documents\\flatt_сертификат.pdf'


    fillpdfs.get_form_fields(pdf_path)

    # returns a dictionary of fields
    # Set the returned dictionary values a save to a variable
    # For radio boxes ('Off' = not filled, 'Yes' = filled)

    data_dict = {
        'fullname': 'Name',
    }

    fillpdfs.write_fillable_pdf(pdf_path, output_pdf_path, data_dict)

    # If you want it flattened:
    fillpdfs.flatten_pdf(output_pdf_path, flatt)
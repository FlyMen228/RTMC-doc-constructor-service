from django.shortcuts import render
from django.http import request, HttpResponse, FileResponse


def index(request: request) -> HttpResponse:
    
    test_abs_pdf_path = r"C:\Users\PC\Desktop\Сашина хуйня\RTMC\RTMC-doc-constructor-service\RTMC\Сonstructor\documents\сертификат.pdf"
    
    context = {
        'pdf_file_path' : test_abs_pdf_path
    }
    
    return render(request, 'index.html', context)
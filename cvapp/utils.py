# cvapp/utils.py
from io import BytesIO
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from django.http import HttpResponse

def render_to_pdf(template_src, context_dict={}):
    html = render_to_string(template_src, context_dict)
    result = BytesIO()
    pdf = pisa.CreatePDF(src=html, dest=result)
    if pdf.err:
        return None
    return result.getvalue()  # bytes

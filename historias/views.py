from django.http import HttpResponse
# from reports import ReportHistoria
from .reports import generar_reporte_medico
#from geraldo.generators import PDFGenerator
from .models import Consulta
from .models import Medico

# def historia_report(request):
#     resp = HttpResponse(mimetype='application/pdf')
#     consultas = Consulta.objects.order_by('date_consulta')
#     report = ReportHistoria(queryset=consultas)
#     report.generate_by(PDFGenerator, filename=resp)
#     return resp

def medico_report(request, object_id):
    print(request)
    medico = Medico.objects.filter(pk= object_id).first()
    return generar_reporte_medico(request, medico)

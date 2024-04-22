from django.template.loader import render_to_string
from django.http import HttpResponse

from weasyprint import HTML

from .models import Medico
from .models import Paciente
from .models import Consulta


def generar_reporte_medico(request, medico: Medico):

    print(request.user)

    file_name = 'list_people.pdf'

    # parsea el template con el contexto
    html_string = render_to_string('reporte_medico.html', {'medico' : medico})
    html = HTML(string = html_string)
    result = html.write_pdf(file_name)
    
    # Creating http response
    with open(file_name, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename={0}'.format(file_name)
        return response


def generar_reporte_historia_clinica(request, paciente: Paciente):

    medico = Medico.objects.filter(usuario_id=request.user.pk).order_by('numero_documento').first()
    # parsea el template con el contexto
    file_name = 'paciente.pdf'

    consultas = paciente.historias_consulta_paciente.all()
    html_string = render_to_string('reporte_historia_medica.html', 
                                   {'medico': medico, 'paciente' : paciente, 'consultas': consultas})
    html = HTML(string = html_string, base_url=request.build_absolute_uri())
    result = html.write_pdf(file_name)


    # Creating http response
    with open(file_name, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename={0}'.format(file_name)
        return response

def generar_reporte_consulta(request, consulta: Consulta):

    medico = Medico.objects.filter(usuario_id=request.user.pk).order_by('numero_documento').first()
    # parsea el template con el contexto
    file_name = 'consulta.pdf'

    paciente = Paciente.objects.filter(pk=consulta.paciente.id).first()
    consultas = []
    consultas.append(consulta)
    html_string = render_to_string('reporte_consulta.html', 
                                   {'medico': medico, 
                                    'paciente' : paciente, 
                                    'consultas': consultas})
    html = HTML(string = html_string, base_url=request.build_absolute_uri())
    result = html.write_pdf(file_name)


    # Creating http response
    with open(file_name, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename={0}'.format(file_name)
        return response


def generar_reporte_formula_medica(request, consulta: Consulta):

    medico = Medico.objects.filter(usuario_id=request.user.pk).order_by('numero_documento').first()
    # parsea el template con el contexto
    file_name = 'formula_medica.pdf'

    paciente = Paciente.objects.filter(pk=consulta.paciente.id).first()
    diagnostico = consulta.historias_consultadiagnostico_consulta.first()

    html_string = render_to_string('reporte_formula_medica.html', 
                                   {'medico': medico, 
                                    'paciente' : paciente, 
                                    'consulta': consulta,
                                    'diagnostico': diagnostico})
    html = HTML(string = html_string, base_url=request.build_absolute_uri())
    result = html.write_pdf(file_name)


    # Creating http response
    with open(file_name, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename={0}'.format(file_name)
        return response


def generar_reporte_examenes(request, consulta: Consulta):

    medico = Medico.objects.filter(usuario_id=request.user.pk).order_by('numero_documento').first()
    # parsea el template con el contexto
    file_name = 'examenes.pdf'

    paciente = Paciente.objects.filter(pk=consulta.paciente.id).first()
    diagnostico = consulta.historias_consultadiagnostico_consulta.first()

    html_string = render_to_string('reporte_examenes.html', 
                                   {'medico': medico, 
                                    'paciente' : paciente, 
                                    'consulta': consulta,
                                    'diagnostico': diagnostico})
    html = HTML(string = html_string, base_url=request.build_absolute_uri())
    result = html.write_pdf(file_name)


    # Creating http response
    with open(file_name, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename={0}'.format(file_name)
        return response


def generar_reporte_certificacion(request, consulta: Consulta):

    medico = Medico.objects.filter(usuario_id=request.user.pk).order_by('numero_documento').first()
    # parsea el template con el contexto
    file_name = 'certificacion.pdf'

    paciente = Paciente.objects.filter(pk=consulta.paciente.id).first()
    consultas = []
    consultas.append(consulta)
    html_string = render_to_string('reporte_certificacion.html', 
                                   {'medico': medico, 
                                    'paciente' : paciente, 
                                    'consultas': consultas})
    html = HTML(string = html_string, base_url=request.build_absolute_uri())
    result = html.write_pdf(file_name)


    # Creating http response
    with open(file_name, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename={0}'.format(file_name)
        return response


def generar_reporte_incapacidad(request, consulta: Consulta):

    medico = Medico.objects.filter(usuario_id=request.user.pk).order_by('numero_documento').first()
    # parsea el template con el contexto
    file_name = 'incapacidad.pdf'

    paciente = Paciente.objects.filter(pk=consulta.paciente.id).first()
    consultas = []
    consultas.append(consulta)
    html_string = render_to_string('reporte_incapacidad_medica.html', 
                                   {'medico': medico, 
                                    'paciente' : paciente, 
                                    'consultas': consultas})
    html = HTML(string = html_string, base_url=request.build_absolute_uri())
    result = html.write_pdf(file_name)


    # Creating http response
    with open(file_name, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename={0}'.format(file_name)
        return response


def generar_reporte_interconsulta(request, consulta: Consulta):

    medico = Medico.objects.filter(usuario_id=request.user.pk).order_by('numero_documento').first()
    # parsea el template con el contexto
    file_name = 'interconsulta.pdf'

    paciente = Paciente.objects.filter(pk=consulta.paciente.id).first()
    consultas = []
    consultas.append(consulta)
    html_string = render_to_string('reporte_interconsulta.html', 
                                   {'medico': medico, 
                                    'paciente' : paciente, 
                                    'consultas': consultas})
    html = HTML(string = html_string, base_url=request.build_absolute_uri())
    result = html.write_pdf(file_name)


    # Creating http response
    with open(file_name, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename={0}'.format(file_name)
        return response

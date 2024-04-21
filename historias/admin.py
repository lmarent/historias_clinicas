from historias.models import Medico
from historias.models import Genero
from historias.models import EstadoCivil
from historias.models import TipoDocumento
from historias.models import RiesgoPaciente
from historias.models import OrigenAtencion
from historias.models import ViaIngreso
from historias.models import CodigoTriage
from historias.models import ViasSuministroMedicamento
from historias.models import TiempoUso
from historias.models import CausaExterna
from historias.models import Medicamento
from historias.models import CertezaDiagnostico
from historias.models import Diagnostico
from historias.models import Entidades
from historias.models import Paciente
from historias.models import Consulta
from historias.models import Ocupacion
from historias.models import Municipio
from historias.models import TipoAntecedente
from historias.models import TipoExamenFisico
from historias.models import Paraclinico
from historias.models import ConsultaAntecedentes
from historias.models import ConsultaDiagnostico
from historias.models import ConsultaExamenFisico
from historias.models import ConsultaParaclinicos
from historias.models import ConsultaFormulacion
from historias.models import ConsultaTratamiento
from django.contrib import admin 
from django.http import HttpResponseRedirect
from django.contrib import admin

from django.http import HttpResponse
from .reports import generar_reporte_medico
from .reports import generar_reporte_historia_clinica
from .reports import generar_reporte_consulta
from .reports import generar_reporte_formula_medica
from .reports import generar_reporte_examenes
from .reports import generar_reporte_certificacion
from .reports import generar_reporte_incapacidad
from .reports import generar_reporte_interconsulta
# from historias.reports import ReportParaclinicos
#from geraldo.generators import PDFGenerator



class ButtonAdmin(admin.ModelAdmin):

    change_buttons=[]
    list_buttons=[]

    def button_view_dispatcher(self, request, url):
        # Dispatch the url to a function call
        print('in button_view_dispatcher', url)
        if url is not None:
            import re
            res = re.match('(.*/)?(?P<id>\d+)/(?P<command>.*)/(?P<button_command>.*)', url)
            if res:
                print('in 1', res.group('button_command'), 'asdasd')
                print([b.func_name for b in self.change_buttons])
                if res.group('button_command') in [b.func_name for b in self.change_buttons]:
                    print('in 4')

                    obj = self.model._default_manager.get(pk=res.group('id'))
                    print(dir(self))
                    response = getattr(self, res.group('button_command'))(request, obj)
                    
                    if response is None:
                        from django.http import HttpResponseRedirect
                        return HttpResponseRedirect(request.META['HTTP_REFERER'])
                    return response
            else:
                res = re.match('(.*/)?(?P<command>.*)', url)
                print('in 2')
                if res:
                    if res.group('command') in [b.func_name for b in self.list_buttons]:
                        response = getattr(self, res.group('command'))(request)
                        if response is None:
                            from django.http import HttpResponseRedirect
                            return HttpResponseRedirect(request.META['HTTP_REFERER'])
                        return response
        # Delegate to the appropriate method, based on the URL.
        from django.contrib.admin.utils import unquote
        if url is None:
            return self.changelist_view(request)
        elif url == "add":
            return self.add_view(request)
        elif url.endswith('/history'):
            return self.history_view(request, unquote(url[:-8]))
        elif url.endswith('/delete'):
            return self.delete_view(request, unquote(url[:-7]))
        else:
            return self.change_view(request, unquote(url))

    def get_urls(self):
        from django.conf.urls import url
        from functools import update_wrapper
        
        # Define a wrapper view
        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            return update_wrapper(wrapper, view)
        
        #  Add the custom button url
        urlpatterns = [
            url(r'^(.+)/$', wrap(self.button_view_dispatcher))
        ]
        return urlpatterns + super(ButtonAdmin, self).get_urls()

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if not extra_context: extra_context = {}
        if hasattr(self, 'change_buttons'):
            extra_context['buttons'] = self._convert_buttons(self.change_buttons)
        if '/' in object_id:
            object_id = object_id[:object_id.find('/')]
        return super(ButtonAdmin, self).change_view(request, object_id, form_url, extra_context)

    def changelist_view(self, request, extra_context=None):
        if not extra_context: extra_context = {}
        if hasattr(self, 'list_buttons'):
            extra_context['buttons'] = self._convert_buttons(self.list_buttons)
        return super(ButtonAdmin, self).changelist_view(request, extra_context)
        
    def _convert_buttons(self, orig_buttons):
        buttons = []
        for b in orig_buttons:
            print('b.func_name', b.func_name)
            buttons.append({ 'func_name': b.func_name, 'short_description': b.short_description })
        return buttons


class MedicoAdmin(ButtonAdmin):
    fieldsets = [
        ('Identificacion',               {'fields': ('tipo_documento',('numero_documento','registro_medico'),'especialidad', 'usuario')  }),
        ('Nombres', {'fields': (('primer_nombre', 'segundo_nombre'),('primer_apellido','segundo_apellido')) 
                    }),
        ('Datos de contacto', {'fields': (('telefono', 'direccion', 'ciudad'),
                                         ),
                                           
                               }),

    ]

    def bar(self, request, obj=None):
        if obj != None: obj.bar()
        return None # Redirect or Response or None
    
    bar.short_description='Reporte del medico inscrito'
    bar.func_name='Reporte'
    list_buttons = [ bar ]
    change_buttons = [ bar ]
    
    def Reporte(self, request, obj):
        medico = Medico.objects.filter(pk= obj.pk).order_by('numero_documento').first()
        return generar_reporte_medico(request, medico)   


admin.site.register(RiesgoPaciente)
admin.site.register(OrigenAtencion)
admin.site.register(ViaIngreso)
admin.site.register(CodigoTriage)
admin.site.register(ViasSuministroMedicamento)
admin.site.register(TiempoUso)
admin.site.register(CausaExterna)
admin.site.register(Medico,MedicoAdmin)
admin.site.register(Genero)
admin.site.register(EstadoCivil)
admin.site.register(TipoDocumento)
admin.site.register(CertezaDiagnostico)
admin.site.register(Diagnostico)
admin.site.register(Medicamento)
admin.site.register(Entidades)
admin.site.register(Ocupacion)
admin.site.register(Municipio)
admin.site.register(TipoAntecedente)
admin.site.register(TipoExamenFisico)
admin.site.register(Paraclinico)


class PacienteAdmin(ButtonAdmin):
    fieldsets = [
        ('Identificacion',               {'fields': ('tipo_documento','numero_documento')  }),
        ('Nombres', {'fields': (('primer_nombre', 'segundo_nombre'),('primer_apellido','segundo_apellido')) 
                    }),
        ('Datos Personales primarios', {'fields': (('sexo','estado_civil','ocupacion'),('fecha_nacimiento', 'lugar_nacimiento')) 
                                       }), 
        ('Datos Persona Responsable',  {'fields': (('persona_responsable','tel_responsable'))
                                       }),                               
        ('Datos de contacto', {'fields': (('telefono_casa', 'direccion_casa', 'ciudad_casa'), 
                                          ('telefono_oficina', 'direccion_oficina', 'ciudad_oficina')),
                                          'classes': ['collapse']  
                                         }),
        ('Afiliacion', {'fields': ('entidad', 'codigo_contrato','fecha_alta'), 
                        'classes': ['collapse']  
                       }),
    ]
    list_filter = ['primer_apellido' ]
    search_fields = ['primer_apellido', 'primer_nombre', 'segundo_nombre', 'numero_documento']
    def bar(self, request, obj=None):
        if obj != None: obj.bar()
        return None # Redirect or Response or None
    bar.short_description='Reporte'
    bar.func_name='Reporte'
    list_buttons = [ bar ]
    change_buttons = [ bar ]
    
    def Reporte(self, request, obj):
        return generar_reporte_historia_clinica(request, obj)    
    
    
admin.site.register(Paciente, PacienteAdmin)


class AntecedentesInline(admin.StackedInline):
    model = ConsultaAntecedentes
    extra = 1
    classes = ['collapse']

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class DiagnosticoInline(admin.StackedInline):
    model = ConsultaDiagnostico
    extra = 1
    classes = ['collapse']

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ConsultaExamenFisicoInline(admin.StackedInline):
    model = ConsultaExamenFisico
    extra = 1
    classes = ['collapse']

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ConsultaParaclinicosInline(admin.StackedInline):
    model = ConsultaParaclinicos
    extra = 1
    classes = ['collapse']

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ConsultaFormulacionInline(admin.TabularInline):
    model = ConsultaFormulacion
    extra = 1
    classes = ['collapse']

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ConsultaTratamientoInline(admin.TabularInline):
    model = ConsultaTratamiento
    max_num = 1
    classes = ['collapse']

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ConsultaAdmin(ButtonAdmin):
    fieldsets = [
        (None, {'fields': ('paciente', ('date_consulta','hora'),('motivo','enfermedad_actual'), 
                          ('certificacion', 'interconsulta'), ('incapacidad_medica', ))}),
    ]
    inlines = [AntecedentesInline, ConsultaExamenFisicoInline, ConsultaParaclinicosInline, 
                DiagnosticoInline, ConsultaFormulacionInline, ConsultaTratamientoInline ]

    class Media:
         js = ['js/jquery.js',]

    #list_filter = ['paciente' ]
    search_fields = ['paciente__numero_documento', 'paciente__primer_apellido','paciente__primer_nombre','paciente__segundo_nombre']

    def bar(self, request, obj=None):
        if obj != None: obj.bar()
        return None # Redirect or Response or None
    bar.short_description='Reporte'
    bar.func_name='Reporte'
    
    def bar2(self, request, obj=None):
        if obj != None: obj.bar2()
        return None # Redirect or Response or None
    bar2.short_description='Formula'
    bar2.func_name='Formula'

    def bar3(self, request, obj=None):
        if obj != None: obj.bar3()
        return None # Redirect or Response or None
    bar3.short_description='Paraclinicos'
    bar3.func_name='Paraclinicos'

    def bar4(self, request, obj=None):
        if obj != None: obj.bar4()
        return None # Redirect or Response or None
    bar4.short_description='Certificacion'
    bar4.func_name='Certificacion'

    def bar5(self, request, obj=None):
        if obj != None: obj.bar5()
        return None # Redirect or Response or None
    bar5.short_description='Incapacidad'
    bar5.func_name='Incapacidad'

    def bar6(self, request, obj=None):
        if obj != None: obj.bar6()
        return None # Redirect or Response or None
    bar6.short_description='Interconsulta'
    bar6.func_name='Interconsulta'

    
    list_buttons = [ bar, bar2, bar3, bar4, bar5, bar6 ]
    change_buttons = [ bar, bar2, bar3, bar4, bar5, bar6 ]
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "paciente":
            kwargs["queryset"] = Paciente.objects.order_by('numero_documento')
            return db_field.formfield(**kwargs)
        return super(ConsultaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
        
    def Reporte(self, request, obj):
        return generar_reporte_consulta(request, obj)

    def Formula(self, request, obj):
        return generar_reporte_formula_medica(request, obj)

    def Paraclinicos(self, request, obj):
        return generar_reporte_examenes(request, obj)

    def Certificacion(self, request, obj):
        return generar_reporte_certificacion(request, obj)

    def Incapacidad(self, request, obj):
        return generar_reporte_incapacidad(request, obj)

    def Interconsulta(self, request, obj):
        return generar_reporte_interconsulta(request, obj)

    def get_readonly_fields(self, request, obj=None):
        "Una vez se crea la consulta y se guarda no debe dejarse modificar"
        if obj is not None:
            ro = [f.name for f in self.model._meta.fields]
            return ro

        return self.readonly_fields


admin.site.register(Consulta, ConsultaAdmin)


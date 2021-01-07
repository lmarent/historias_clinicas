from django.db import models
from datetime import datetime
from datetime import date
import sys
import os
import csv 
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.

class Ocupacion(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.nombre
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Ocupacion'
        verbose_name_plural = 'Ocupaciones'


class RiesgoPaciente(models.Model):
    codigo = models.CharField(max_length=3)
    nombre = models.CharField(max_length=255)

    def __unicode__(self):
        return self.codigo + ' ' + self.nombre

    def __str__(self):
        return self.codigo + ' ' + self.nombre

    class Meta:
        verbose_name = 'Riesgo Paciente'
        verbose_name_plural = 'Riesgo de Paciente'    


class CausaExterna(models.Model):
    codigo = models.CharField(max_length=3)
    nombre = models.CharField(max_length=255)

    def __unicode__(self):
        return self.codigo + ' ' + self.nombre

    def __str__(self):
        return self.codigo + ' ' + self.nombre

    class Meta:
        verbose_name = 'Causa Externa'
        verbose_name_plural = 'Causas Externas'    


class ViasSuministroMedicamento(models.Model):
    nombre = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Via de suministro'
        verbose_name_plural = 'Vias de suministro'    


class TiempoUso(models.Model):
    nombre = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tiempo de Uso Medicamento'
        verbose_name_plural = 'Tiempos de uso de Medicamento'        


class TipoAntecedente(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tipo de antecedente'
        verbose_name_plural = 'Tipos de Antecedentes'


class TipoExamenFisico(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tipo de examen fisico'
        verbose_name_plural = 'Tipos de examenes fisicos'


class Paraclinico(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return str(self.pk) + ' ' + self.nombre

    def nombre_impreso(self):
        return self.nombre

    class Meta:
        verbose_name = 'Paraclinico'
        verbose_name_plural = 'Paraclinicos'
     

class Municipio(models.Model):
    nombre = models.CharField(max_length=255)
    codigo_dian = models.CharField(max_length=5)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
    

class EstadoCivil(models.Model):
    nombre = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Estado Civil'
        verbose_name_plural = 'Estados Civiles'


# se debe reemplazar por impresion diagnostica
class CertezaDiagnostico(models.Model):
    nombre = models.CharField(max_length=50)
    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre
     

class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre
    

class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre


    class Meta:
        verbose_name = 'Tipo de documento'
        verbose_name_plural = 'Tipos de documentos'


class OrigenAtencion(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Origen de Atencion'
        verbose_name_plural = 'Origenes de atencion'


class ViaIngreso(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Via de Ingreso'
        verbose_name_plural = 'Vias de Ingreso'


class CodigoTriage(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Codigo Triage'
        verbose_name_plural = 'Codigos Triage'


class Medico(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    primer_nombre = models.CharField(max_length=40)
    segundo_nombre = models.CharField(max_length=40)
    primer_apellido = models.CharField(max_length=40)
    segundo_apellido = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=20)
    direccion = models.CharField(max_length=60)
    ciudad = models.ForeignKey(Municipio, 
                               related_name="%(app_label)s_%(class)s_medico", 
                               on_delete=models.PROTECT)
    telefono = models.CharField(max_length=15)
    tipo_documento = models.ForeignKey(TipoDocumento,                                
                                        related_name="%(app_label)s_%(class)s_tipo_documento", 
                                        on_delete=models.PROTECT)
    numero_documento = models.CharField(max_length=15)
    registro_medico = models.CharField(max_length=15)

    def __unicode__(self):
        return self.primer_nombre + ' ' + self.segundo_nombre + ' ' + self.primer_apellido + ' ' + self.segundo_apellido 

    def __str__(self):
        return self.primer_nombre + ' ' + self.segundo_nombre + ' ' + self.primer_apellido + ' ' + self.segundo_apellido 
        
    def nombre_impreso(self):
        return self.nombres() + ' ' + self.apellidos() 

    def nombres(self):
        if self.segundo_nombre:
            return self.primer_nombre + ' ' + self.segundo_nombre
        else:
            return self.primer_nombre

    def apellidos(self):
        if self.segundo_apellido:
            return self.primer_apellido + ' ' + self.segundo_apellido
        else:
            return self.primer_apellido


class Medicamento(models.Model):
    nombre = models.CharField(max_length=80)
    dosis = models.CharField(max_length=60)
    nota = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'


class Diagnostico(models.Model):
    codigo_int = models.CharField('ICD-10', max_length=4)
    nombre = models.CharField('Enfermedad',max_length=255)

    def __unicode__(self):
        return self.codigo_int + ' - ' + self.nombre

    def __str__(self):
        return self.nombre
        
    def ingresoDatos():
        csv_filepathname="C:\Historias\hist\historias\Enfermedades.csv"
        dataReader = csv.reader(open(csv_filepathname), delimiter=';', quotechar='"')
        for row in dataReader:
            if row[0] != 'CODIGO': # Ignore the header row, import everything else
                diagnostico = Diagnostico()
                diagnostico.codigo_int = row[0]
                diagnostico.nombre = row[1]
                diagnostico.save()        
    
    class Meta:
        verbose_name = 'Diagnostico'
        verbose_name_plural = 'Diagnosticos'


class Entidades(models.Model):
    nombre = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Entidad'
        verbose_name_plural = 'Entidades'


class Entidades_Planes(models.Model):
    entidad = models.ForeignKey(Entidades, 
                                related_name="%(app_label)s_%(class)s_entidad", 
                                on_delete=models.PROTECT)
    tipo_plan = models.CharField(max_length=2)
    subplan = models.CharField(max_length=4)
    descripcion = models.CharField(max_length=255)

    def __unicode__(self):
        return self.entidad

    def __str__(self):
        return self.nombre


class Paciente(models.Model):
    tipo_documento = models.ForeignKey(TipoDocumento, 
                                        related_name="%(app_label)s_%(class)s_tipo_documento", 
                                        on_delete=models.PROTECT)
    numero_documento = models.CharField(max_length=15)
    primer_nombre = models.CharField(max_length=40)
    segundo_nombre = models.CharField(max_length=40)
    primer_apellido = models.CharField(max_length=40)
    segundo_apellido = models.CharField(max_length=40)
    sexo = models.ForeignKey(Genero, 
                              related_name="%(app_label)s_%(class)s_genero", 
                                on_delete=models.PROTECT)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento')
    lugar_nacimiento = models.ForeignKey(Municipio, 
                                         related_name="lugar_nacimiento",
                                         on_delete=models.PROTECT)
    ocupacion = models.ForeignKey(Ocupacion, 
                                    related_name="%(app_label)s_%(class)s_ocupacion", 
                                        on_delete=models.PROTECT)
    estado_civil = models.ForeignKey(EstadoCivil, 
                                      related_name="%(app_label)s_%(class)s_estado_civil", 
                                        on_delete=models.PROTECT)
    ciudad_casa = models.ForeignKey(Municipio, 
                                    related_name="ciudad_residencia",
                                     on_delete=models.PROTECT)
    telefono_casa = models.CharField(max_length=12)
    direccion_casa = models.CharField(max_length=40)    
    ciudad_oficina = models.ForeignKey(Municipio, 
                                        related_name="ciudad_trabajo",
                                         on_delete=models.PROTECT)
    telefono_oficina = models.CharField(max_length=12)
    direccion_oficina = models.CharField(max_length=40)    
    entidad = models.ForeignKey(Entidades, 
                                related_name="%(app_label)s_%(class)s_entidad", 
                                on_delete=models.PROTECT)
    codigo_contrato = models.CharField(max_length=15) 
    persona_responsable = models.CharField(max_length=60)
    tel_responsable = models.CharField(max_length=12)
    fecha_alta = models.DateField('Fecha de creacion')
    
    def __unicode__(self):
        return self.numero_documento + '-' + self.primer_nombre + ' ' + self.segundo_nombre + ' ' + self.primer_apellido + ' ' + self.segundo_apellido 
    
    def __str__(self):
        return self.numero_documento + '-' + self.primer_nombre + ' ' + self.segundo_nombre + ' ' + self.primer_apellido + ' ' + self.segundo_apellido 

    def nombres(self):
        if self.segundo_nombre:
            return self.primer_nombre + ' ' + self.segundo_nombre
        else:
            return self.primer_nombre

    def apellidos(self):
        if self.segundo_apellido:
            return self.primer_apellido + ' ' + self.segundo_apellido
        else:
            return self.primer_apellido

    def edad(self):
        hoy = date.today()
        return hoy.year - self.fecha_nacimiento.year - ((hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))


class Consulta(models.Model):
    # finalidad de la consulta
    paciente = models.ForeignKey(Paciente, 
                                 related_name="%(app_label)s_%(class)s_paciente", 
                                    on_delete=models.PROTECT)
    date_consulta = models.DateField(default=now, blank=True)
    hora = models.TimeField('Hora de Consulta', default=now, blank=True)
    motivo = models.TextField()
    enfermedad_actual = models.TextField()
    certificacion = models.TextField(blank=True, null=True)
    interconsulta = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.paciente.primer_nombre + ' ' + self.paciente.segundo_nombre + ' ' + self.paciente.primer_apellido + ' ' +  self.paciente.segundo_apellido + ' ' + self.date_consulta.strftime("%d/%m/%y")

    def __str__(self):
        return self.paciente.primer_nombre + ' ' + self.paciente.segundo_nombre + ' ' + self.paciente.primer_apellido + ' ' +  self.paciente.segundo_apellido + ' ' + self.date_consulta.strftime("%d/%m/%y")
    

class ConsultaAntecedentes(models.Model):
    consulta = models.ForeignKey(Consulta, 
                                 related_name="%(app_label)s_%(class)s_consulta", 
                                 on_delete=models.PROTECT)
    tipo_antecedentes = models.ForeignKey(TipoAntecedente, 
                                          related_name="%(app_label)s_%(class)s_tipo_antecedente", 
                                          on_delete=models.PROTECT)
    texto_encontrado = models.TextField('Antecedente Encontrado')

    def __unicode__(self):
        return self.tipo_antecedentes.nombre

    def __str__(self):
        return self.tipo_antecedentes.nombre

    class Meta:
        verbose_name = 'Antecedente'
        verbose_name_plural = 'Antecedentes'
        

class ConsultaDiagnostico(models.Model):
    consulta = models.ForeignKey(Consulta, 
                                  related_name="%(app_label)s_%(class)s_consulta", 
                                  on_delete=models.PROTECT)
    # se debe reemplazar por impresion diagnostica
    certeza = models.ForeignKey(CertezaDiagnostico, 
                                 related_name="%(app_label)s_%(class)s_certeza_diagnostico", 
                                  on_delete=models.PROTECT) 
    diagnostico_principal = models.ForeignKey(Diagnostico, related_name="Principal", on_delete=models.PROTECT)
    diagnostico_secundario1 = models.ForeignKey(Diagnostico, related_name="Secundario1", on_delete=models.PROTECT)
    diagnostico_secundario2 = models.ForeignKey(Diagnostico, related_name="Secundario2", on_delete=models.PROTECT)
    riesgo_paciente = models.ForeignKey(RiesgoPaciente, 
                                        related_name="%(app_label)s_%(class)s_riesgo_paciente", 
                                        on_delete=models.PROTECT)
    explicacion = models.TextField()
    causa_externa = models.ForeignKey(CausaExterna, 
                                       related_name="%(app_label)s_%(class)s_causa_externa", 
                                        on_delete=models.PROTECT)
    origen_atencion = models.ForeignKey(OrigenAtencion, 
                                        related_name="%(app_label)s_%(class)s_origen_atencion", 
                                        on_delete=models.PROTECT)
    via_ingreso = models.ForeignKey(ViaIngreso, 
                                    related_name="%(app_label)s_%(class)s_via_ingreso", 
                                    on_delete=models.PROTECT)
    codigo_triage = models.ForeignKey(CodigoTriage, 
                                      related_name="%(app_label)s_%(class)s_codigo_triage", 
                                      on_delete=models.PROTECT)
    def __unicode__(self):
        return self.diagnostico_principal.nombre

    def __str__(self):
        return self.diagnostico_principal.nombre

    class Meta:
        verbose_name = 'Diagnostico'
        verbose_name_plural = 'Diagnosticos'

# se necesita una clase de revision por sistemas

class ConsultaExamenFisico(models.Model):
    consulta = models.ForeignKey(Consulta, 
                                 related_name="%(app_label)s_%(class)s_consulta", 
                                 on_delete=models.PROTECT)
    tipo_examen = models.ForeignKey(TipoExamenFisico, 
                                    related_name="%(app_label)s_%(class)s_tipo_examen", 
                                    on_delete=models.PROTECT)
    texto_encontrado = models.TextField('Revision efectuada')

    def __unicode__(self):
        return self.tipo_examen.nombre

    def __str__(self):
        return self.tipo_examen.nombre

    class Meta:
        verbose_name = 'Examen Fisico'
        verbose_name_plural = 'Examenes Fisicos'


class ConsultaParaclinicos(models.Model):
    consulta = models.ForeignKey(Consulta, 
                                  related_name="%(app_label)s_%(class)s_consulta", 
                                   on_delete=models.PROTECT)
    paraclinico = models.ForeignKey(Paraclinico,
                                    related_name="%(app_label)s_%(class)s_paraclinico", 
                                     on_delete=models.PROTECT)
    texto_encontrado = models.TextField('Examen Solicitado')
    
    def __unicode__(self):
        return self.paraclinico.nombre        

    def __str__(self):
        return self.paraclinico.nombre        

    class Meta:
        verbose_name = 'Paraclinico'
        verbose_name_plural = 'Paraclinicos'


class ConsultaFormulacion(models.Model):
    consulta = models.ForeignKey(Consulta, 
                                  related_name="%(app_label)s_%(class)s_consulta", 
                                     on_delete=models.PROTECT)
    nombre_del_medicamento = models.CharField(max_length=60)    
    cantidad =  models.IntegerField()    
    vias_suministro_medicamento = models.ForeignKey(ViasSuministroMedicamento, 
                                   related_name="%(app_label)s_%(class)s_vias_suministro_medicamento", 
                                     on_delete=models.PROTECT)
    dosificacion = models.CharField(max_length=250)
    tiempoUso = models.ForeignKey(TiempoUso, 
                                    related_name="%(app_label)s_%(class)s_tiempo_uso", 
                                     on_delete=models.PROTECT)
    class Meta:
        verbose_name = 'Formulacion'
        verbose_name_plural = 'Formulaciones'


class ConsultaTratamiento(models.Model):
    consulta = models.ForeignKey(Consulta, 
                                   related_name="%(app_label)s_%(class)s_consulta", 
                                     on_delete=models.PROTECT)
    tratamiento = models.TextField()
    
    def __unicode__(self):
        return self.tratamiento
    
    def __str__(self):
        return self.tratamiento

    class Meta:
        verbose_name = 'Tratamiento'
        verbose_name_plural = 'Tratamientos'
    
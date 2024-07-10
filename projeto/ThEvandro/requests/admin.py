from django.contrib import admin
from .models import Certificado, RegistroHoraAcademica

@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('nome_evento', 'estudante', 'data_evento', 'horas', 'data_envio')
    search_fields = ('nome_evento', 'estudante__username', 'data_evento')
    list_filter = ('data_evento', 'horas')

@admin.register(RegistroHoraAcademica)
class RegistroHoraAcademicaAdmin(admin.ModelAdmin):
    list_display = ('certificado', 'aprovado', 'revisado_por', 'data_revisao')
    search_fields = ('certificado__nome_evento', 'revisado_por__username')
    list_filter = ('aprovado', 'data_revisao')

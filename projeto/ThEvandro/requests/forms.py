from django import forms
from .models import Certificado
from django.core.exceptions import ValidationError

def validar_pdf(arquivo):
    if not arquivo.name.endswith('.pdf'):
        raise ValidationError("Apenas arquivos PDF são permitidos.")
    if arquivo.size > 10*1024*1024:  # limite de tamanho do arquivo para 10MB
        raise ValidationError("O tamanho do arquivo deve ser menor que 10MB.")

class FormularioEnvioCertificado(forms.ModelForm):
    arquivo_certificado = forms.FileField(validators=[validar_pdf])

    class Meta:
        model = Certificado
        fields = ['nome_evento', 'data_evento', 'horas', 'arquivo_certificado']

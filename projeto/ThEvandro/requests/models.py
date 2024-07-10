from django.db import models
from django.contrib.auth.models import User

class Certificado(models.Model):
    estudante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificados')
    nome_evento = models.CharField(max_length=255)
    data_evento = models.DateField()
    horas = models.PositiveIntegerField()
    arquivo_certificado = models.FileField(upload_to='arquivos_certificados/')
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome_evento} - {self.estudante.username}"

class RegistroHoraAcademica(models.Model):
    certificado = models.OneToOneField(Certificado, on_delete=models.CASCADE, related_name='registro_hora_academica')
    aprovado = models.BooleanField(default=False)
    revisado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='certificados_revisados')
    data_revisao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.certificado.nome_evento} - {self.aprovado}"

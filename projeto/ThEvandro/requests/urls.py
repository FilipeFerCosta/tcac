from django.urls import path
from . import views

app_name = 'requerimentos'

urlpatterns = [
    path("", views.PainelView.as_view(), name="homepage"),
    path("enviar/", views.EnviarCertificadoView.as_view(), name="enviar_certificado"),
    path("revisar/", views.RevisarCertificadosView.as_view(), name="revisar_certificados"),
    path("aprovar/<int:certificado_id>/", views.AprovarCertificadoView.as_view(), name="aprovar_certificado"),
    path("rejeitar/<int:certificado_id>/", views.RejeitarCertificadoView.as_view(), name="rejeitar_certificado"),
]

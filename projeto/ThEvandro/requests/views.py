from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from .models import Certificado, RegistroHoraAcademica
from .forms import FormularioEnvioCertificado
from django.utils import timezone


class PainelView(LoginRequiredMixin, View):
    template_name = 'apps/requests/index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            certificados = Certificado.objects.filter(registro_hora_academica__isnull=True)
        else:
            certificados = Certificado.objects.filter(estudante=request.user)
        form = FormularioEnvioCertificado()
        context = {
            'certificados': certificados,
            'form': form,
        }
        return render(request, self.template_name, context)



class EnviarCertificadoView(LoginRequiredMixin, FormView):
    template_name = 'apps/requests/certificados/enviar_certificado.html'
    form_class = FormularioEnvioCertificado
    success_url = reverse_lazy('requerimentos:homepage')

    def form_valid(self, form):
        certificado = form.save(commit=False)
        certificado.estudante = self.request.user
        certificado.save()
        return super().form_valid(form)

class RevisarCertificadosView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Certificado
    template_name = 'apps/requests/certificados/revisar_certificados.html'
    context_object_name = 'certificados'

    def test_func(self):
        return self.request.user.is_staff

    def get_queryset(self):
        return Certificado.objects.filter(registro_hora_academica__isnull=True)

class AprovarCertificadoView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff

    def post(self, request, certificado_id):
        certificado = Certificado.objects.get(id=certificado_id)
        RegistroHoraAcademica.objects.create(
            certificado=certificado,
            aprovado=True,
            revisado_por=request.user,
            data_revisao=timezone.now()
        )
        return redirect('revisar_certificados')

class RejeitarCertificadoView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff

    def post(self, request, certificado_id):
        certificado = Certificado.objects.get(id=certificado_id)
        RegistroHoraAcademica.objects.create(
            certificado=certificado,
            aprovado=False,
            revisado_por=request.user,
            data_revisao=timezone.now()
        )
        return redirect('revisar_certificados')

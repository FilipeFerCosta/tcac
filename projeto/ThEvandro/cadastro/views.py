from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import CadastrarUsuario

class Cadastro(TemplateView):
    template_name = "apps/cadastro/index.html"
    
    def get(self, request, *args, **kwargs):
        form = CadastrarUsuario()
        context = {'registerform': form}
        return self.render_to_response(context)
    
    def post(self, request, *args, **kwargs):
        form = CadastrarUsuario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login:login')
        context = {'registerform': form}
        return self.render_to_response(context)

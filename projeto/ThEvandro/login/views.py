from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.views import LogoutView as DjangoLogoutView


class LoginView(TemplateView):
    template_name = "apps/login/index.html"

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        context = {'loginform': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home:homepage')  # Mudar quando implementar o dashboard para o dashboard
            else:
                form.add_error(None, "Invalid username or password")
        context = {'loginform': form}
        return self.render_to_response(context)

class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy('login:login')  

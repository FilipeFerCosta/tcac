from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class HomeView(LoginRequiredMixin, TemplateView):
    staticpage = "apps/home/index.html"

    def get_template_names(self):
        return "apps/home/index.html"

    def landing_page_view(request):
        return render(request, 'index.html')
    

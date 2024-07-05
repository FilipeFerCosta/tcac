from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    staticpage = "apps/home/index.html"

    def get_template_names(self):
        return "apps/home/index.html"

    def landing_page_view(request):
        return render(request, 'index.html')
    
    
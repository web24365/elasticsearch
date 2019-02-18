from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class index(TemplateView):
    template_name = "elastic/index.html"

# def index(request):
#     return render(request, 'elastic/index.html')
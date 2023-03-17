from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from setting.models import Setting

from .models import *

class ServicesView(TemplateView):
    template_name = "services/services.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all().order_by('id')[:7]
        context['settings'] = Setting.objects.all().order_by('id')[:1]
        return context
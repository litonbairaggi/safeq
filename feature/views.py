from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render

from .models import Feature
from setting.models import Setting

class FeatureView(TemplateView):
    template_name = "feature/feature.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['features'] = Feature.objects.order_by('id')[:1]
        context['settings'] = Setting.objects.all().order_by('id')[:1]
        return context
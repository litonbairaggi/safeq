from django.shortcuts import render
from django.views.generic import TemplateView
from .models import AboutUs, FounderInfo, AboutTime
from setting.models import Setting

# Create your views here.

class AboutUsView(TemplateView):
    template_name = "about/about.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_uss'] = AboutUs.objects.all().order_by('id')[:1]
        context['founder_infos'] = FounderInfo.objects.all().order_by('id')[:1]
        context['about_times'] = AboutTime.objects.all().order_by('id')[:1]
        
        context['settings'] = Setting.objects.all().order_by('id')[:1]
        return context
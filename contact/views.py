from django.shortcuts import render
from django.views.generic import TemplateView
from .models import HotlineInfo, OfficeAddress
from setting.models import Setting

# Create your views here.

class ContactInfoView(TemplateView):
    template_name = "contact/contact.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotline_infos'] = HotlineInfo.objects.order_by('id')[:1]
        context['office_address'] = OfficeAddress.objects.order_by('id')[:1]
        context['settings'] = Setting.objects.all().order_by('id')[:1]
        return context
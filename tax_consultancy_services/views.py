from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render

from .models import ServiceTC, CardTC, CustomerBenefitTC
from setting.models import Setting
class ServiceView(TemplateView):
    template_name = "tax_consultancy_services/tax_consultancy_services.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['service_tcs'] = ServiceTC.objects.order_by('id')[:1]
        context['card_tcs'] = CardTC.objects.order_by('id')[:1]
        context['customer_benefit_tcs'] = CustomerBenefitTC.objects.order_by('id')[:1]
        context['settings'] = Setting.objects.all().order_by('id')[:1]
        return context
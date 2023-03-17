from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ServiceHS, CardHS, CustomerBenefitHS
from setting.models import Setting
# Create your views here.

class ServiceHSView(TemplateView):
    template_name = "hr_support/hr_support.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['service_hss'] = ServiceHS.objects.order_by('id')[:1]
        context['card_hss'] = CardHS.objects.order_by('id')[:1]
        context['customer_benefit_hss'] = CustomerBenefitHS.objects.order_by('id')[:1]
        context['settings'] = Setting.objects.all().order_by('id')[:1]
        return context
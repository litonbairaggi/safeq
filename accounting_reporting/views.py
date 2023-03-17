from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render

from accounting_reporting.models import ServiceAR, CardAR, CustomerBenefitAR
from setting.models import Setting

class ServiceARView(TemplateView):
    template_name = "accounting_reporting/accounting_reporting.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['service_ars'] = ServiceAR.objects.order_by('id')[:1]
        context['card_ars'] = CardAR.objects.order_by('id')[:1]
        context['customer_benefit_ars'] = CustomerBenefitAR.objects.order_by('id')[:1]
        
        context['settings'] = Setting.objects.all().order_by('id')[:1]
        return context
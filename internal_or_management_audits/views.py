from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ServiceIMA, CardIMA, CustomerBenefitIMA
from setting.models import Setting

# Create your views here.

class ServiceIMAView(TemplateView):
    template_name = "internal_or_management_audits/internal_or_management_audits.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['service_imas'] = ServiceIMA.objects.order_by('id')[:1]
        context['card_imas'] = CardIMA.objects.order_by('id')[:1]
        context['customer_benefit_imas'] = CustomerBenefitIMA.objects.order_by('id')[:1]
        context['settings'] = Setting.objects.all().order_by('id')[:1]
        return context
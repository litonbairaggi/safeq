from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ServiceCM, CardCM, CustomerBenefitCM
from setting.models import Setting
# Create your views here.

class ServiceCMView(TemplateView):
    template_name = "compliance_management/compliance_management.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['service_cms'] = ServiceCM.objects.order_by('id')[:1]
        context['card_cms'] = CardCM.objects.order_by('id')[:1]
        context['customer_benefit_cms'] = CustomerBenefitCM.objects.order_by('id')[:1]
        context['settings'] = Setting.objects.all().order_by('id')[:1]
        return context
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ServiceCO, CardCO, CustomerBenefitCO
from setting.models import Setting
# Create your views here.

class ServiceCOView(TemplateView):
    template_name = "comprehensive_outsourcing/comprehensive_outsourcing.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['service_cos'] = ServiceCO.objects.order_by('id')[:1]
        context['card_cos'] = CardCO.objects.order_by('id')[:1]
        context['customer_benefit_cos'] = CustomerBenefitCO.objects.order_by('id')[:1]
        context['settings'] = Setting.objects.all().order_by('id')[:1]
        return context
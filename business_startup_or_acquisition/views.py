from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ServiceBSA, CardBSA, CustomerBenefitBSA
from setting.models import Setting

# Create your views here.

class ServiceBSAView(TemplateView):
    template_name = "business_startup_or_acquisition/business_s_or_a.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['service_bsas'] = ServiceBSA.objects.order_by('id')[:1]
        context['card_bsas'] = CardBSA.objects.order_by('id')[:1]
        context['customer_benefit_bsas'] = CustomerBenefitBSA.objects.order_by('id')[:1]
        context['settings'] = Setting.objects.all().order_by('id')[:1]
        
        return context
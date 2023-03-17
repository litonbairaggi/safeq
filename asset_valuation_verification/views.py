from django.shortcuts import render
from django.views.generic import TemplateView
from asset_valuation_verification.models import ServiceAVV, CardAVV, CustomerBenefitAVV
from setting.models import Setting
# Create your views here.

class ServiceAVVView(TemplateView):
    template_name = "asset_valuation_verification/asset_valuation_verification.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['service_avvs'] = ServiceAVV.objects.order_by('id')[:1]
        context['card_avvs'] = CardAVV.objects.order_by('id')[:1]
        context['customer_benefit_avvs'] = CustomerBenefitAVV.objects.order_by('id')[:1]
        
        context['settings'] = Setting.objects.all().order_by('id')[:1]
        return context
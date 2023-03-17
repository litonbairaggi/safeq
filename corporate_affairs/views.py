from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render

from .models import ServiceCA, CardCA, CustomerBenefitCA
from setting.models import Setting

class ServiceCAView(TemplateView):
    template_name = "corporate_affairs/corporate_affairs.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['service_cas'] = ServiceCA.objects.order_by('id')[:1]
        context['card_cas'] = CardCA.objects.order_by('id')[:1]
        context['customer_benefit_cas'] = CustomerBenefitCA.objects.order_by('id')[:1]
        context['settings'] = Setting.objects.all().order_by('id')[:1]
        return context
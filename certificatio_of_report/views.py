from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render

from certificatio_of_report.models import ServiceCR, CardCR, CustomerBenefitCR
from setting.models import Setting

class ServiceCRView(TemplateView):
    template_name = "certificatio_of_report/certificatio_of_report.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['service_crs'] = ServiceCR.objects.order_by('id')[:1]
        context['card_crs'] = CardCR.objects.order_by('id')[:1]
        context['customer_benefit_crs'] = CustomerBenefitCR.objects.order_by('id')[:1]
        context['settings'] = Setting.objects.all().order_by('id')[:1]

        return context
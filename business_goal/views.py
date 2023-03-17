from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render

from .models import BusinessGoal
from setting.models import Setting
class BusinessGoalView(TemplateView):
    template_name = "business_goal/business_goal.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['goals'] = BusinessGoal.objects.order_by('id')[:1]
        context['settings'] = Setting.objects.all().order_by('id')[:1]
        return context
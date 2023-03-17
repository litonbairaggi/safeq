from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

# from .models import Blog
from news_and_update.models import NewsUpdate
from feature.models import Feature
from our_clients.models import OurClient
from service.models import Service
from setting.models import Setting
from slider.models import Slider
from business_goal.models import BusinessGoal
from counter.models import Counter
from teams .models import Teams
from about.models import AboutUs, FounderInfo, AboutTime

class HomeView(TemplateView):
    template_name = "index/index.html"
    # template_name_base = "base/base.html"
    
    # def get_template_names(self):
    #     if some_condition:
    #         return [self.template_name_base]
    #     else:
    #         return [self.template_name]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['services'] = Service.objects.all().order_by('id')[:7]
        # if template_name == "base/base.html":
        
        
        context['settings'] = Setting.objects.all().order_by('id')[:1]
        context['sliders'] = Slider.objects.all().order_by('id')[:3]
        context['counters'] = Counter.objects.all().order_by('id')[:4]
        
        context['about_uss'] = AboutUs.objects.all().order_by('id')[:1]
        context['founder_infos'] = FounderInfo.objects.all().order_by('id')[:1]
        context['about_times'] = AboutTime.objects.all().order_by('id')[:1]
        
        # Our Trusted Clients 
        context['our_clients'] = OurClient.objects.all().order_by('id')[:7]
        context['teams'] = Teams.objects.all().order_by('id')[:7]
        context['goals'] = BusinessGoal.objects.order_by('id')[:1]
        context['features'] = Feature.objects.order_by('id')[:1]
        context['news_updates'] = NewsUpdate.objects.all().order_by('id')[:7]
        return context 
    
    
    # def get_template_names(self):
    #     if self.kwargs.get('pk'):
    #         return [self.team_profile_template_name]
    #     return super().get_template_names()

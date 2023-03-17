from django.views.generic import TemplateView
from .models import NewsUpdate
from setting.models import Setting

class NewsUpdateView(TemplateView):
    template_name = "news_and_update/news_update.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_updates'] = NewsUpdate.objects.all().order_by('id')[:7]
        context['settings'] = Setting.objects.all().order_by('id')[:1]
        return context
    
class NewsUpdateDetailView(TemplateView):
    template_name = "news_and_update/detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nu_details'] = NewsUpdate.objects.all().order_by('id')[:7]
        context['settings'] = Setting.objects.all().order_by('id')[:1]
        return context
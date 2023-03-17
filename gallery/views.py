from django.views.generic import TemplateView
from .models import Gallery
from setting.models import Setting

class GalleryView(TemplateView):
    template_name = "gallery/gallery.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallerys'] = Gallery.objects.all().order_by('id')[:7]
        context['settings'] = Setting.objects.all().order_by('id')[:1]
        return context
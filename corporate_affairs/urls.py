from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.ServiceCAView.as_view(), name="service_ca"),
]
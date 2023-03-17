from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.NewsUpdateView.as_view(), name="news_update"),
    path('detail/<int:pk>/',views.NewsUpdateDetailView.as_view(), name="nu_detail"),
]
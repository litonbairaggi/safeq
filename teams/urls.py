from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.TeamsView.as_view(), name="teams"),
    path('detail/<int:pk>/',views.TeamsDetailView.as_view(), name="team_detail"),
]
from django.contrib import admin
from .models import Feature

# Register your models here.


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['id', 'feature_img', 'pre_title', 'title', 'description', 'feature_1', 'feature_2', 'feature_3', 'feature_4']
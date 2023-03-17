from django.contrib import admin
from .models import Counter
# Register your models here.

@admin.register(Counter)
class CounterAdmin(admin.ModelAdmin):
    list_display = ['id', 'value_1', 'subject_1', 'value_2', 'subject_2', 'value_3', 'subject_3', 'value_4', 'subject_4']
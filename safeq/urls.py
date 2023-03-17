from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView.as_view(), name="home"),

    path('slider/', include('slider.urls')),
    path('about/', include('about.urls')),
    path('', include('setting.urls')),
    path('services/', include('service.urls')),
    path('services/tax-consultancy/', include('tax_consultancy_services.urls')),
    path('services/accounting-reporting/', include('accounting_reporting.urls')),
    path('services/corporate-affairs/', include('corporate_affairs.urls')),
    path('services/internal/management-audits/', include('internal_or_management_audits.urls')),
    path('services/compliance-management/', include('compliance_management.urls')),
    path('services/certificatio-report/', include('certificatio_of_report.urls')),
    path('services/asset-valuation-verification/', include('asset_valuation_verification.urls')),
    path('services/comprehensive-outsourcing/', include('comprehensive_outsourcing.urls')),
    path('services/business-startup-acquisition/', include('business_startup_or_acquisition.urls')),
    path('services/hr-support/', include('hr_support.urls')),
    path('our-clients/', include('our_clients.urls')),
    path('teams/', include('teams.urls')),
    path('business-goal/', include('business_goal.urls')),
    path('counter/', include('counter.urls')),
    path('feature/', include('feature.urls')),
    path('news-&-update/', include('news_and_update.urls')),
    path('contact/', include('contact.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

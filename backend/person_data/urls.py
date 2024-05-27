from django.urls import path
from . import views


urlpatterns = [
    path('personal_info/', views.personal_info, name='personal_info'),
    path('success/', views.success, name='success'),
    path('', views.company_info, name='company_info'),
]

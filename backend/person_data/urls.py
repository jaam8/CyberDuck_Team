from django.urls import path
from . import views


urlpatterns = [
    path('personal_info/', views.personal_info, name='personal_info'),
    path('success/', views.success, name='success'),
    path('physical_face/', views.physical_face, name='physical_face'),
    path('legal_face/', views.legal_face, name='legal_face'),
    path('', views.choice, name='choice'),
    # path('', views.company_info, name='company_info'),
]

from django.urls import path
from person_data import views


urlpatterns = [
    path('', views.login)
]

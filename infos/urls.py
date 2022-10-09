
from django.urls import path
from . import views

urlpatterns = [
    path('infos/', views.infos),
    path('me/', views.me),
    path('contact/', views.contact),
]

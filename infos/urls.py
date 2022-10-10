
from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.me),
    path('contact/', views.contact),

]

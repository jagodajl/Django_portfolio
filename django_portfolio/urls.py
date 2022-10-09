
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = {
    path('admin/', admin.site.urls),
    path('infos/', include('infos.urls')),
    path('me/', include('infos.urls')),
    path('contact/', include('infos.urls')),
    path('', views.portfolio),
}

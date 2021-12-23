from django.conf.urls import include
from django.urls import path

from django.contrib import admin
admin.autodiscover()
from projectApp import views

urlpatterns = [
    path('user/', include('userApp.urls')),
    path('admin/', admin.site.urls),
    path('projects/', include('projectApp.urls')),
    path('about', views.aboutPage),
    path('', views.homepage),
]

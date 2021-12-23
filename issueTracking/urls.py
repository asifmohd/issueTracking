from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()
from projectApp import views

urlpatterns = [
    url(r'^user/', include('userApp.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^projects/', include('projectApp.urls')),
    url(r'^about', views.aboutPage),
    url(r'^$', views.homepage),
]

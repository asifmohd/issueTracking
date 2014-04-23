from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from projectApp import views

urlpatterns = patterns('',
    url(r'^user/', include('userApp.urls', namespace='userApp')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^projects', include('projectApp.urls', namespace='projectApp')),
    url(r'^about', views.aboutPage),
    url(r'^$', views.homepage),
)

from django.conf.urls import url

from userApp import views

app_name = 'userApp'
urlpatterns = [
                url(r'^login/', views.login, name='login'),
                url(r'^signup/', views.register, name = 'register'),
                url(r'^profile/', views.profile, name='profile'),
                url(r'^logout/', views.logoutUser, name='logoutUser'),
    ]

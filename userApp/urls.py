from django.urls import path

from userApp import views

app_name = 'userApp'
urlpatterns = [
                path('login/', views.login, name='login'),
                path('signup/', views.register, name = 'register'),
                path('profile/', views.profile, name='profile'),
                path('logout/', views.logoutUser, name='logoutUser'),
    ]

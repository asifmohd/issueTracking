from django.urls import path

from projectApp import views

app_name = 'projectApp'
urlpatterns = [
                path('create/', views.createProject, name='createProject'),
                path('downvote/<int:pk>/', views.downvoteRequest, name='downvoteRequestUrl'),
                path('upvote/<int:pk>/', views.upvoteRequest, name='upvoteRequestUrl'),
                path('<int:pk>/issues/create/', views.createIssue, name='createIssue'),
                path('<int:pk>/issues/', views.IssueIndexView.as_view(), name='issuesIndex'),
                path('issue/<int:pk>/', views.IssueDetailView.as_view(), name='issueDetails'),
                path('<int:pk>/', views.ProjectDetailView.as_view(), name='projectDetails'),
                path('', views.ProjectIndexView.as_view(), name='projectsIndex'),
    ]


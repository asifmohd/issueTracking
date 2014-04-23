from django.conf.urls import patterns, url

from projectApp import views

urlpatterns = patterns('',
                url(r'^/create$', views.createProject, name='createProject'),
                url(r'/downvote/(?P<pk>\d+)/$', views.downvoteRequest, name='downvoteRequestUrl'),
                url(r'/upvote/(?P<pk>\d+)/$', views.upvoteRequest, name='upvoteRequestUrl'),
                url(r'^/(?P<pk>\d+)/issues/create$', views.createIssue, name='createIssue'),
                url(r'/(?P<pk>\d+)/issues$', views.IssueIndexView.as_view(), name='issuesIndex'),
                url(r'/issue/(?P<pk>\d+)$', views.IssueDetailView.as_view(), name='issueDetails'),
                url(r'/(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name='projectDetails'),
                # url(r'/search/(?P<pk>\s+)/$', views.search, name='searchPage'),
                url(r'^$', views.ProjectIndexView.as_view(), name='projectsIndex'),
    )


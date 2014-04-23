from django.contrib import admin

from projectApp.models import Project, Issue, Comment, Vote
# Register your models here.
admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Comment)
admin.site.register(Vote)

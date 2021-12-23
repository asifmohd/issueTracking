from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone

from django.contrib.auth.models import User
from projectApp.models import Project, Issue, Comment

from django import forms
from django.template import RequestContext

class IssueForm(forms.Form):
    issueName = forms.CharField(label='', max_length=200, widget=forms.TextInput(attrs={'autofocus':'autofocus', 'placeholder': 'Issue Name'}))
    stepsToReproduce = forms.CharField(label='', max_length=5000, widget=forms.Textarea(attrs={'rows':5, 'cols':80, 'placeholder': 'Steps To Reproduce'}))

class CommentForm(forms.Form):
    comment = forms.CharField(label='', max_length=5000, widget=forms.Textarea(attrs={'rows':5, 'cols':80, 'placeholder': 'Comment'}))

class ProjectForm(forms.Form):
    name = forms.CharField(label='', max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Project Name'}))
    details = forms.CharField(label='', max_length=5000, widget=forms.Textarea(attrs={'rows':10, 'cols':40, 'placeholder': 'Project Details'}))


class ProjectIndexView(generic.ListView):
    template_name = 'projectApp/projects.html'
    context_object_name = 'projects_list'

    def get_queryset(self):
        return Project.objects.all()

class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'projectApp/projectDetails.html'
    def get_queryset(self):
        return Project.objects.all()

class IssueDetailView(generic.DetailView):
    model = Issue
    template_name = 'projectApp/issueDetails.html'
    def get_queryset(self):
        return Issue.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IssueDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        print request.POST
        commentText = request.POST["comment"]
        newComment = Comment(comment=commentText, time=timezone.now(), commentedOn=self.get_object(), commentedBy=request.user)
        newComment.save()
        return HttpResponseRedirect('')
        # return HttpResponse("Succefully commented")


class IssueIndexView(generic.ListView):
    template_name = 'projectApp/issues.html'
    context_object_name = 'issues_list'

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs['pk'])

@login_required(login_url="/user/login/")
def createProject(request):
    c = RequestContext(request)
    c.update(csrf(request))
    projectName = projectDetails = ''
    if request.POST:
        form = ProjectForm(request.POST)
        if form.is_valid():
            projectName = form.cleaned_data['name']
            projectDetails = form.cleaned_data['details']
            currentUser = User.objects.get(username=request.user)
            # try:
            newProject = Project(name=projectName, details=projectDetails, createdOn=timezone.now(), createdBy=currentUser)
            newProject.save()
            # except:
                # return HttpResponse("Error occurred.")
            # return HttpResponse("You have successfully created a project.")
            return HttpResponseRedirect("projects/" + str(newProject.id))
    else:
        form = ProjectForm()
    c['form'] = form
    return render_to_response('projectApp/createProject.html', c)

@login_required(login_url="/user/login/")
def createIssue(request, pk):
    c = RequestContext(request)
    c.update(csrf(request))
    if request.POST:
        form = IssueForm(request.POST)
        if form.is_valid():
            issueName = form.cleaned_data['issueName']
            steps = form.cleaned_data['stepsToReproduce']
            reportedOn = timezone.now()
            project = Project.objects.get(pk=pk)
            newIssue = Issue(project=project, issueName=issueName, stepsToReproduce=steps, reportedOn=reportedOn, reportedBy=request.user)
            newIssue.save()
            # return HttpResponse("successfully created a new issue")
            return HttpResponseRedirect("projects/" + str(project.id))
    else:
        form = IssueForm()
    c['form'] = form
    return render_to_response('projectApp/createIssue.html', c)

def homepage(request):
    return render_to_response('projectApp/home.html', context_instance=RequestContext(request))
    # return HttpResponse("this is the homepage")

def aboutPage(request):
    return render_to_response('projectApp/about.html', context_instance=RequestContext(request))

def search(request):
    return HttpResponse("Search page")

@login_required(login_url="/user/login/")
def downvoteRequest(request, pk):

    print "Inside downvoteRequest with pk = ", pk
    return HttpResponseRedirect('/projects/' + str(Issue.objects.get(pk=pk).project_id))

@login_required(login_url="/user/login/")
def upvoteRequest(request, pk):
    print request.user
    print "Inside upvoteRequest with pk = ", pk
    return HttpResponseRedirect('/projects/' + str(Issue.objects.get(pk=pk).project_id))

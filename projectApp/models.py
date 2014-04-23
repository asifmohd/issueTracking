from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    details = models.CharField(max_length=5000)
    createdOn = models.DateTimeField('Project Created on')
    createdBy = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

class Issue(models.Model):
    project = models.ForeignKey(Project)
    issueName = models.CharField(max_length=200)
    stepsToReproduce = models.CharField(max_length=5000)
    votes = models.IntegerField(default=0)
    reportedOn = models.DateTimeField('Issue Reported On')
    reportedBy = models.ForeignKey(User)

    def __unicode__(self):
        return self.issueName

    def calculateVotes(self):
        issueVote = Vote.objects.filter(votedOn = self.id)
        total = 0
        for i in issueVote:
            total += i.value
        return total

    def hasUserVoted(self, currentUser):
        issueVote = Vote.objects.filter(votedOn = self.id)
        users = [i.user.username for i in issueVote]
        if currentUser in users:
            return True
        else:
            return False


class Comment(models.Model):
    comment = models.CharField(max_length=5000)
    time = models.DateTimeField('Commented on')
    commentedOn = models.ForeignKey(Issue)
    commentedBy = models.ForeignKey(User)

    def __unicode__(self):
        return self.comment

class Vote(models.Model):
    user = models.ForeignKey(User)
    votedOn = models.ForeignKey(Issue)
    value = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.username + " voted on " + self.votedOn.issueName + " with value = " + str(self.value)

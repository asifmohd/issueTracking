from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    details = models.CharField(max_length=5000)
    createdOn = models.DateTimeField('Project Created on')
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Issue(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    issueName = models.CharField(max_length=200)
    stepsToReproduce = models.CharField(max_length=5000)
    votes = models.IntegerField(default=0)
    reportedOn = models.DateTimeField('Issue Reported On')
    reportedBy = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
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
    commentedOn = models.ForeignKey(Issue, on_delete=models.CASCADE)
    commentedBy = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    votedOn = models.ForeignKey(Issue, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username + " voted on " + self.votedOn.issueName + " with value = " + str(self.value)

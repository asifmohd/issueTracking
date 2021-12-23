from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=200, primary_key=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.email

class Detail(models.Model):
    email = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name

from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=55, default="", null=True)
    email = models.EmailField(default="", null=True)
    phone_number = models.IntegerField(default=None, null=True)
    student_class = models.IntegerField(default=None, null=True)
    age = models.IntegerField(default=None, null=True)
    bio = models.TextField(null=True, blank=True, default="")
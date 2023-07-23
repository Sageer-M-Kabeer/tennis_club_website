from django.db import models
from django.utils import timezone

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(auto_now_add=timezone.now(),null=True)
  slug = models.SlugField(default="", null=False,blank=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"
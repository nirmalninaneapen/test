from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
class User(AbstractUser):
    class Meta:
        db_table = "users"
class Team(models.Model):
    name = models.CharField(max_length=50, null=True,blank=True)
    coach = models.CharField(max_length=50, null=True,blank=True)
    manager = models.CharField(max_length=50, null=True,blank=True)
    class Meta:
        db_table = "teams"
class Member(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True,blank=True)
    class Meta:
        db_table = "members"
class Venue(models.Model):
    name = models.CharField(max_length=50, null=True,blank=True)
    class Meta:
        db_table = "venues"
class Goal(models.Model):
    goal = models.CharField(max_length=50, null=True,blank=True)
    teamid = models.CharField(max_length=50, null=True, blank=True)
    class Meta:
        db_table = "goals"
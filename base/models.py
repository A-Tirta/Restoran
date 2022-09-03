from email.message import Message
from django.db import models

# Create your models here.

class BookTable(models.Model):
  Name = models.CharField(max_length=255)
  Email = models.EmailField()
  Phone = models.CharField(max_length=13)
  Date = models.CharField(max_length=13)
  Time = models.CharField(max_length=50)
  ManyPeople = models.CharField(max_length=100)
  Message = models.TextField()

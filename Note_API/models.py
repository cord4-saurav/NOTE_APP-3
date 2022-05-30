from django.db import models
import datetime

# Create your models here.
class NoteAPI(models.Model):
    NoteID = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    now = datetime.datetime.now()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
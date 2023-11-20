from django.db import models
import datetime
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    detail = models.CharField(max_length=500)
    cat = models.IntegerField()
    due_date = models.DateField()
    created_on = models.DateField(default= datetime.datetime.now())
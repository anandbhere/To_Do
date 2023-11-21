from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    detail = models.CharField(max_length=500)
    cat = models.IntegerField()
    due_date = models.DateField()
    created_on = models.DateField(default= datetime.datetime.now())
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
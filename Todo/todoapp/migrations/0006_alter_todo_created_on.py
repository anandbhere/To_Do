# Generated by Django 4.2.2 on 2023-11-22 15:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_alter_todo_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2023, 11, 22, 20, 55, 19, 345872)),
        ),
    ]

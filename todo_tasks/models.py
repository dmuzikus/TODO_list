from django.db import models
from django.db import DataError, IntegrityError
from datetime import datetime
from django.contrib.auth.models import User as Django_user


class TodoTask(models.Model):
    id = models.IntegerField(primary_key=True)
    for_user = models.ForeignKey(Django_user, null=True, on_delete=models.PROTECT, related_name='sectiondata')
    title = models.CharField(max_length=1024)
    group = models.CharField(max_length=128)
    subtasks = models.CharField(max_length=2048, blank=True, null=True)
    is_finished = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        managed = True

from django.db import models
from django.utils import timezone

# Create your models here.
class taskModel(models.Model):
    task_name = models.CharField(max_length=30)
    priority_level = models.CharField(max_length=30)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s %s"%(self.task_name, self.completed)

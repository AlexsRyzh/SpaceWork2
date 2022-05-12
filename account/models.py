from django.db import models
from django.contrib.auth.models import User


class WorkField(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.title

class TaskField(models.Model):
    workField = models.ForeignKey(WorkField, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.title

class Task(models.Model):
    taskField = models.ForeignKey(TaskField, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=1000, default="")
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

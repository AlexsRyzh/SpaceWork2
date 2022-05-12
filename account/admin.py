from django.contrib import admin
from .models import Task, TaskField, WorkField
# Register your models here.
admin.site.register(Task)
admin.site.register(TaskField)
admin.site.register(WorkField)
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import WorkField, TaskField, Task


class WorkFieldForm(ModelForm):
    class Meta:
        model = WorkField
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class TaskFieldForm(ModelForm):
    class Meta:
        model = TaskField
        fields = '__all__'


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

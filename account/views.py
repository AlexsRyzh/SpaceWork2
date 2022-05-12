from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Task, WorkField, TaskField
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, WorkFieldForm, TaskFieldForm, TaskForm
from django.contrib import messages


def registerPage(request):
    form = CreateUserForm(request.POST)
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if (form.is_valid()):
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')

    context = {
        'form': form
    }
    return render(request, 'auth/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.info(request, 'Username Or password is incorrect')
    context = {}
    return render(request, 'auth/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def mainPage(request):
    tasks = Task.objects.all()
    task_fields = TaskField.objects.all()
    work_fields = WorkField.objects.filter(user=request.user)
    context = {
        'tasks': tasks,
        'task_fields': task_fields,
        'work_fields': work_fields,
    }
    return render(request, 'main.html', context)


def work_field(request, workfield):
    tasks = Task.objects.all()
    task_fields = TaskField.objects.all()
    work_fields = WorkField.objects.filter(user=request.user)
    context = {
        'tasks': tasks,
        'task_fields': task_fields,
        'work_fields': work_fields,
        'curren_work_field': workfield
    }
    return render(request, 'work_field/work_field.html', context)


def addWorkFieldPage(request):
    tasks = Task.objects.all()
    task_fields = TaskField.objects.all()
    work_fields = WorkField.objects.filter(user=request.user)
    form = WorkFieldForm()

    if request.method == 'POST':
        form = WorkFieldForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
        return redirect('main')

    context = {
        'tasks': tasks,
        'task_fields': task_fields,
        'work_fields': work_fields,
        'form': form,
    }
    return render(request, 'work_field/add_work_field.html', context)


def editWorkFieldPage(request, pk):
    tasks = Task.objects.all()
    task_fields = TaskField.objects.all()
    work_fields = WorkField.objects.filter(user=request.user)
    work_field1 = WorkField.objects.get(id=pk)
    form = WorkFieldForm(instance=work_field1)
    if request.method == 'POST':
        form = WorkFieldForm(request.POST, instance=work_field1)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('main')

    context = {
        'tasks': tasks,
        'task_fields': task_fields,
        'work_fields': work_fields,
        'form': form,
    }
    return render(request, 'work_field/edite_work_field.html', context)


def deleteWorkFieldPage(request, pk):
    tasks = Task.objects.all()
    task_fields = TaskField.objects.all()
    work_fields = WorkField.objects.filter(user=request.user)
    work_field = WorkField.objects.get(id=pk)
    if (request.method == "POST"):
        work_field.delete()
        return redirect('main')

    context = {
        'tasks': tasks,
        'task_fields': task_fields,
        'work_fields': work_fields,
        'work_field': work_field
    }
    return render(request, 'work_field/delete_work_field.html', context)


def main_activePage(request, pk):
    work_field = WorkField.objects.get(id=pk)
    work_fields = WorkField.objects.filter(user=request.user)
    task_fields = TaskField.objects.filter(workField=work_field)
    tasks = Task.objects.all()
    context = {
        'work_field': work_field,
        'work_fields': work_fields,
        'task_fields': task_fields,
        'tasks': tasks,
    }
    return render(request, 'main_active.html', context)


def addTaskFieldPage(request, pk):
    work_fields = WorkField.objects.filter(user=request.user)
    work_field = WorkField.objects.get(id=pk)
    task_fields = TaskField.objects.filter(workField=work_field)
    tasks = Task.objects.all()
    form = TaskFieldForm()

    if request.method == 'POST':
        form = TaskFieldForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.workField = work_field
            form.save()
        return redirect('main_active', pk)

    context = {
        'work_field': work_field,
        'work_fields': work_fields,
        'task_fields': task_fields,
        'tasks': tasks,
        'task_field_form': form
    }
    return render(request, 'task_field/add_task_field.html', context)


def editTaskFieldPage(request, pk_work_field, pk_task_field):
    work_fields = WorkField.objects.filter(user=request.user)
    work_field = WorkField.objects.get(id=pk_work_field)
    task_fields = TaskField.objects.filter(workField=work_field)
    task_field = TaskField.objects.get(id=pk_task_field)
    tasks = Task.objects.all()
    form = TaskFieldForm(instance=task_field)

    if request.method == 'POST':
        form = WorkFieldForm(request.POST, instance=task_field)
        if form.is_valid():
            form = form.save(commit=False)
            form.workField = WorkField.objects.get(id=pk_work_field)
            form.save()
        return redirect('main_active', pk_work_field)

    context = {
        'work_field': pk_work_field,
        'work_fields': work_fields,
        'task_fields': task_fields,
        'tasks': tasks,
        'task_field_form': form
    }
    return render(request, 'task_field/edit_task_field.html', context)


def deleteTaskFieldPage(request, pk_work_field, pk_task_field):
    work_field = WorkField.objects.get(id=pk_work_field)
    work_fields = WorkField.objects.filter(user=request.user)
    task_fields = TaskField.objects.filter(workField=work_field)
    task_field = TaskField.objects.get(id=pk_task_field)
    tasks = Task.objects.all()
    if (request.method == "POST"):
        task_field.delete()
        return redirect('main_active', pk_work_field)

    context = {
        'work_field': pk_work_field,
        'work_fields': work_fields,
        'task_fields': task_fields,
        'tasks': tasks,
    }
    return render(request, 'task_field/delete_task_field.html', context)


def addTaskPage(request, pk_work_field, pk_task_field):
    work_fields = WorkField.objects.filter(user=request.user)
    work_field = WorkField.objects.get(id=pk_work_field)
    task_fields = TaskField.objects.filter(workField=work_field)
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.taskField = TaskField.objects.get(id=pk_task_field)
            form.save()
        return redirect('main_active', pk_work_field)

    context = {
        'work_field': pk_work_field,
        'work_fields': work_fields,
        'task_fields': task_fields,
        'tasks': tasks,
        'task_form': form
    }
    return render(request, 'task/add_task.html', context)

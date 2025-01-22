from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, TodoItemForm

def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after signup
            return redirect('todo-list')  # Redirect to the to-do list
    else:
        form = SignUpForm()
    return render(request, 'todo_app/sign_up.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('todo-list')  # Redirect to the to-do list
            else:
                form.add_error(None, 'Invalid login credentials')
    else:
        form = AuthenticationForm()
    return render(request, 'todo_app/login.html', {'form': form})

def home(request):
    return render(request, 'todo_app/home.html')

@login_required
def todo_list(request):
    todos = TodoItem.objects.filter(created_by=request.user)  # Filter by user

    return render(request, 'todo_app/todo_list.html', {'todos': todos})

@login_required
def todo_create(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.created_by = request.user
            todo.save()
            return redirect('todo-list')
    else:
        form = TodoItemForm()

    return render(request, 'todo_app/todo_form.html', {'form': form, 'form_title': 'Create Task'})

@login_required
def todo_update(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)

    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo-list')  # Redirect to the list page after saving
    else:
        form = TodoItemForm(instance=todo)

    return render(request, 'todo_app/todo_update.html', {'form': form, 'todo': todo})

@login_required
def todo_delete(request, pk):
    task = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')  # Or wherever you want to redirect after deletion
    return render(request, 'todo_app/confirm_delete.html', {'task': task})
from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def logout_view(request):
    logout(request)
    return redirect('login') 


# Custom login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home after successful login
            else:
                form.add_error(None, 'Invalid login credentials')
    else:
        form = AuthenticationForm()
    return render(request, 'todo_app/login.html', {'form': form})



def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todo-list')  # Redirect to the to-do list or a home page after successful signup
    else:
        form = UserCreationForm()

    return render(request, 'todo_app/sign_up.html', {'form': form})


def home(request):
    return render(request, 'todo_app/home.html')

@login_required
def todo_list(request):
    todos = TodoItem.objects.filter(created_by=request.user)
    return render(request, 'todo_app/todo_list.html', {'todos': todos})

@login_required
def todo_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        TodoItem.objects.create(title=title, description=description, created_by=request.user)
        return redirect('todo-list')
    return render(request, 'todo_app/todo_form.html', {'form_title': 'Create New Task'})

@login_required
def todo_update(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk, created_by=request.user)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
        return redirect('todo-list')
    return render(request, 'todo_app/todo_form.html', {'form_title': 'Edit Task', 'todo': todo})

@login_required
def todo_delete(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk, created_by=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo-list')
    return render(request, 'todo_app/todo_form.html', {'form_title': 'Confirm Deletion', 'todo': todo})

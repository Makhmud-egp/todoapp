from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('', views.home, name='home'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login_view, name='login'),  # Use custom login view
    path('logout/', views.logout_view, name='logout'),
    path('todo/', views.todo_list, name='todo-list'),
    path('todo/create/', views.todo_create, name='todo-create'),
    path('todo/update/<int:pk>/', views.todo_update, name='todo-update'),
     path('delete/<int:pk>/', views.todo_delete, name='todo-delete'),
]
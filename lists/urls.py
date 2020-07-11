from django.urls import path

from lists import views

app_name = 'lists'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/<int:todolist_id>/', views.todolist, name='todolist'),
    path('list/new/', views.new_todolist, name='new_todolist'),
    path('list/add/', views.add_todolist, name='add_todolist'),
    path('todo/add/<int:todolist_id>/', views.add_todo, name='add_todo'),
    path('lists/', views.overview, name='overview'),
]

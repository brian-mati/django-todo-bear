from django.urls import path
from . import  views

urlpatterns = [
    path('create/',views.create_todo_view,name='create_path'),
    path('all_todos/',views.list_todos_view,name="todos_list"),
    path('single_todo/<int:id>/',views.list_single_todo_view,name="single_todo"),
    path('update_todos/<int:id>/',views.update_todos_view,name="update_path"),
    path('test_path/',views.test_view,name="test_path")
]

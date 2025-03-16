from django.urls import path
from . import  views

urlpatterns = [
    path('create/',views.create_todo_view,name='name'),
    path('all_todos/',views.list_todos_view,name="todos_list"),
    path('test_path/',views.test_view,name="test_path")
]

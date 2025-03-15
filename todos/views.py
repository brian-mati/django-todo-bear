from django.shortcuts import render

# Create your views here.

def create_todo_page(request):
    return render(request, "todos/new_todo.html")
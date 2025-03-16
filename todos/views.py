from django.shortcuts import render , redirect
from .forms import TodoForm
from .models import Todo
# Create your views here.

# create todo
def create_todo_view(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos_list')
    
    return render(request,'todos/create_todo.html',{'form':form})



# read todo

def list_todos_view(request):
    todos = Todo.objects.all()
    return render(request,'todos/todos_list.html',{'todos':todos})

def list_single_todo_view(request,id):
    todo = Todo.objects.get(id=id)
    return render(request,'todos/individual_todo.html',{'todo':todo})
# updated todo'

def update_todos_view(request,id):
    todo = Todo.objects.get(id=id)
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos_list')
    return render(request,'todos/update_todo.html',{'form':form})

def test_view(request):
    return render(request,'todos/test_file.html')
# delete todo
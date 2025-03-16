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
            return redirect('')
    
    return render(request,'todos/create_todo.html',{'form':form})



# read todo

def list_todos_view(request):
    todos = Todo.objects.all()
    return render(request,'todos/todos_list.html',{'todos':todos})
# updated todo

def test_view(request):
    return render(request,'todos/test_file.html')
# delete todo
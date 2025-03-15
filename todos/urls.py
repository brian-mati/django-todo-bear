from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
   path('new_todo',views.create_todo_page , name="create_page")
   
]

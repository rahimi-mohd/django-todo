from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages

from .forms import TodoForm
from .models import Todo

# Create your views here.
def home(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            messages.success(request, "Todo Added!")
            return redirect("todo:home")
    else:
        form = TodoForm()

    todos = Todo.objects.filter(user=request.user)

    context = {
        "form": form,
        "todos":todos,
        "title":"Home",
    }

    return render(request, "todo/index.html", context)

def change_status(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if todo.status == 1:
        todo.status = 2
        todo.save()
    elif todo.status == 2:
        todo.delete()
    return redirect("todo:home")
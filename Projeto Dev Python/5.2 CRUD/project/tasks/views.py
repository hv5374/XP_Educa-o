from django.shortcuts import render, redirect
from .forms import TaskForm

# Create your views here.
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('task_create')

    else:
        form = TaskForm()

    return render(request, 'tasks/task_form.html', {'form': form})
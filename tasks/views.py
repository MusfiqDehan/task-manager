from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Task, Photo
from .forms import TaskForm, PhotoForm


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['priorities'] = ['Low', 'Medium', 'High']
        return context

    def get_queryset(self):
        queryset = Task.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query)
            )

        creation_date = self.request.GET.get('creation_date')
        if creation_date:
            queryset = queryset.filter(
                creation_date__date=creation_date
            )

        due_date = self.request.GET.get('due_date')
        if due_date:
            queryset = queryset.filter(
                due_date__date=due_date
            )

        priority = self.request.GET.get('priority')
        if priority:
            queryset = queryset.filter(
                priority=priority
            )

        is_complete = self.request.GET.get('is_complete')
        if is_complete == '1':
            queryset = queryset.filter(is_complete=True)
        elif is_complete == '0':
            queryset = queryset.filter(is_complete=False)

        return queryset


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'


@method_decorator(login_required, name='dispatch')
class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')


@method_decorator(login_required, name='dispatch')
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')


@login_required
def add_photo_to_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.task = task
            photo.save()
            messages.success(request, 'Photo added successfully.')
            return redirect('task_detail', pk=task.pk)
    else:
        form = PhotoForm()
    return render(request, 'tasks/add_photo_to_task.html', {'form': form})


@login_required
def delete_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    task_pk = photo.task.pk
    photo.delete()
    messages.success(request, 'Photo deleted successfully.')
    return redirect('task_detail', pk=task_pk)

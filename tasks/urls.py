from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, add_photo_to_task, delete_photo

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/add_photo/', add_photo_to_task, name='add_photo_to_task'),
    path('delete_photo/<int:pk>/', delete_photo, name='delete_photo'),
]

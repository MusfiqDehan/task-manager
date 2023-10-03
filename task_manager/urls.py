from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from tasks.views import TaskListView
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', TaskListView.as_view(), name='home'),

    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
]

# if settings.DEBUG:
# urlpatterns += static(settings.MEDIA_URL,
#                       document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL,
#                       document_root=settings.STATIC_ROOT)

# urlpatterns += staticfiles_urlpatterns()

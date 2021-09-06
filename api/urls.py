from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import datetime
from . import views
from django.db.models import Q
from django.http import HttpResponse, JsonResponse


router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('get_tasks', views.get_tasks, name='get_tasks'),
    path('change_field', views.change_task_field, name='change_task_field'),
    path('create_task', views.create_task, name='create_task'),
    path('auth_usr', views.check_auth, name='check_auth'),
    path('logout_usr', views.check_logout, name='check_logout'),
    path('get_user', views.get_user_by_session, name='get_user_by_session'),
    path('add_sub', views.add_subtask, name='add_subtask'),
    path('get_history', views.get_history_tasks, name='get_history_tasks')
]

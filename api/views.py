import requests
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import authentication_classes
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

from todo_tasks.models import TodoTask


def get_tasks(request):
    tasks_queryset = TodoTask.objects.filter(is_deleted=False, for_user=User.objects.get(username=request.GET.get('user'))).values()
    tasks_list = [task for task in tasks_queryset]
    my_list = sorted(tasks_list, key=lambda k: k['group'])
    return JsonResponse({'data': my_list})


def get_history_tasks(request):
    tasks_queryset = TodoTask.objects.filter(is_deleted=True, for_user=User.objects.get(username=request.GET.get('user'))).values()
    tasks_list = [task for task in tasks_queryset]
    my_list = sorted(tasks_list, key=lambda k: k['group'])
    return JsonResponse({'data': my_list})


def create_task(request):
    if request.method == 'GET':
        task_title = request.GET.get('title')
        task_group = request.GET.get('group')
        user = request.GET.get('user')
        TodoTask.objects.create(title=task_title, group=task_group, for_user=User.objects.get(username=user))
        return JsonResponse({'data': 'ok'})


def change_task_field(request):
    if request.method == 'GET':
        task_id = request.GET.get('id')
        task_field = request.GET.get('field')
        task_value = request.GET.get('value')
        TodoTask.objects.filter(id=task_id).update(**{str(task_field): str(task_value)})
        return JsonResponse({'data': 'ok'})


def add_subtask(request):
    if request.method == 'GET':
        task_id = request.GET.get('id')
        task_value = request.GET.get('value')
        TodoTask.objects.filter(id=task_id).update(**{'subtasks': (TodoTask.objects.get(id=task_id).subtasks if TodoTask.objects.get(id=task_id).subtasks else '') +str(task_value)+','})
        return JsonResponse({'data': 'ok'})


@csrf_exempt
@authentication_classes([SessionAuthentication, BasicAuthentication])
def check_auth(request):
    print('Аунтефикация в auth_usr')
    if request.method == 'POST':
        try:
            authmeth, auth = request.META['HTTP_AUTHORIZATION'].split(' ', 1)
            print(request.body.decode('utf-8'))
            username, password = auth.split(' ')
            print(username, password)
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
            print('User = ', user)
        except Exception:
            user = None
            print('User = ', user)
        if user:
            print(user)
            request.session['user_authed'] = user.username
            print(request.session.session_key)
            response = JsonResponse({'status': 'logged', 'user': str(request.user), 'is_personal': request.user.is_staff,
                                 'is_superuser': request.user.is_superuser, 'session_id': request.session.session_key}, safe=False)
            response.set_cookie('session_id', request.session.session_key)
            return response
        else:
            return JsonResponse({'status': 'Not_logged'}, safe=False)
    elif request.method == 'GET':
        if request.user.is_authenticated():
            print('USER IS AUTHENTICATED OR HAS SESSION DATA')
            response = JsonResponse({'status': 'logged', 'user': str(request.user), 'is_personal': request.user.is_staff,
                                 'is_superuser': request.user.is_superuser, 'session_id': request.session.session_key}, safe=False)
            response.set_cookie('session_id', request.session.session_key)
            return response
        else:
            return JsonResponse({'status': 'Not_logged'}, safe=False)


@csrf_exempt
def check_logout(request):
    print('Logout...')
    try:
        print('Deleting cookies...')
        del request.session['user_authed']
    except KeyError:
        pass
    print('Sending response...')
    response = JsonResponse({'status': 'Not_logged'}, safe=False)
    return response


@csrf_exempt
@authentication_classes([SessionAuthentication, BasicAuthentication])
def get_user_by_session(request):
    session = Session.objects.get(session_key=request.GET.get('session_id'))
    session_data = session.get_decoded()
    uid = session_data.get('_auth_user_id')
    user = User.objects.get(id=uid)
    return JsonResponse({'data': user.username})


from django.contrib import admin
from .models import TodoTask


@admin.register(TodoTask)
class TodoTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'for_user', 'title', 'group', 'subtasks', 'is_finished', 'is_deleted')
    search_fields = ('id', 'title', 'group')

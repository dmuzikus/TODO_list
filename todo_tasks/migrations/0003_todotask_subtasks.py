# Generated by Django 3.2.7 on 2021-09-06 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_tasks', '0002_todotask_for_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='todotask',
            name='subtasks',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
    ]

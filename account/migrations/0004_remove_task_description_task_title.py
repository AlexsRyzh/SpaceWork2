# Generated by Django 4.0.4 on 2022-05-09 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_task_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
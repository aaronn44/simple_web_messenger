# Generated by Django 4.0.3 on 2022-04-21 13:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('msgr', '0002_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='join',
            name='unread_count',
        ),
        migrations.AddField(
            model_name='join',
            name='last_active',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

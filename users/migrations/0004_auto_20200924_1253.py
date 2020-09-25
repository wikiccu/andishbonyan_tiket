# Generated by Django 3.1 on 2020-09-24 09:23

from django.db import migrations
import django.utils.timezone
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200924_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='replytask',
            name='date',
        ),
        migrations.RemoveField(
            model_name='replytiket',
            name='date',
        ),
        migrations.RemoveField(
            model_name='task',
            name='date',
        ),
        migrations.RemoveField(
            model_name='tiket',
            name='date',
        ),
        migrations.AddField(
            model_name='replytask',
            name='datetime',
            field=django_jalali.db.models.jDateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='replytiket',
            name='datetime',
            field=django_jalali.db.models.jDateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='task',
            name='datetime',
            field=django_jalali.db.models.jDateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='tiket',
            name='datetime',
            field=django_jalali.db.models.jDateTimeField(default=django.utils.timezone.now),
        ),
    ]

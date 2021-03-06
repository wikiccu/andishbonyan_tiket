# Generated by Django 3.1 on 2020-09-24 08:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200916_1308'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tiket',
            options={'ordering': ['-id'], 'verbose_name': 'تیکت', 'verbose_name_plural': 'تیکت ها'},
        ),
        migrations.AddField(
            model_name='replytask',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='replytiket',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='tiket',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

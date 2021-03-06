# Generated by Django 3.1 on 2020-09-16 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='replytask',
            options={'ordering': ['user'], 'verbose_name': 'پاسخ به وظیفه', 'verbose_name_plural': 'پاسخ ها به وظایف'},
        ),
        migrations.AlterModelOptions(
            name='replytiket',
            options={'ordering': ['user'], 'verbose_name': 'پاسخ به تیکت', 'verbose_name_plural': 'پاسخ ها به تیکت ها'},
        ),
        migrations.RenameField(
            model_name='replytask',
            old_name='wuser',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='replytiket',
            old_name='wuser',
            new_name='user',
        ),
    ]

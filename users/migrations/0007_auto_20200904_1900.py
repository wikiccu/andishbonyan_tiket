# Generated by Django 3.1 on 2020-09-04 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200904_1847'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inqueries',
            options={'ordering': ['-vaziat'], 'verbose_name': 'تیکت', 'verbose_name_plural': 'تیکت ها'},
        ),
        migrations.AlterModelOptions(
            name='reply',
            options={'ordering': ['wuser'], 'verbose_name': 'پاسخ', 'verbose_name_plural': 'پاسخ ها'},
        ),
    ]
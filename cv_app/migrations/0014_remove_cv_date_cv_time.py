# Generated by Django 4.1.3 on 2022-12-02 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0013_cv_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='date',
        ),
        migrations.AddField(
            model_name='cv',
            name='time',
            field=models.DateTimeField(default='2022，12，02 02:58'),
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-02 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0012_remove_cv_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='date',
            field=models.DateField(default='2022，12，02 02:57'),
        ),
    ]

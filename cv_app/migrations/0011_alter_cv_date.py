# Generated by Django 4.1.3 on 2022-12-02 02:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0010_remove_cv_time_cv_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='date',
            field=models.DateField(default=datetime.date(2022, 12, 2)),
        ),
    ]

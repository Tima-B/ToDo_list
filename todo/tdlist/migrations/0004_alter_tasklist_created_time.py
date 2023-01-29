# Generated by Django 4.1.5 on 2023-01-27 18:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tdlist", "0003_alter_tasklist_created_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tasklist",
            name="created_time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 1, 27, 23, 14, 2, 210123),
                help_text="Дата создения задачи",
            ),
        ),
    ]

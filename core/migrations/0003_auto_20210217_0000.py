# Generated by Django 3.1.6 on 2021-02-17 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210216_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='finish_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

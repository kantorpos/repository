# Generated by Django 3.2.9 on 2021-12-08 15:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='repo',
            name='date_upload',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

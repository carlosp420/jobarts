# Generated by Django 3.1.2 on 2020-11-08 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='apply',
            new_name='job_url',
        ),
    ]

# Generated by Django 5.1.1 on 2024-10-29 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0018_jobmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobmodel',
            old_name='Job_Image',
            new_name='job_image',
        ),
    ]
# Generated by Django 5.0 on 2023-12-29 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VideoSystem', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videoupload',
            name='Upload_user',
        ),
        migrations.DeleteModel(
            name='VideoComment',
        ),
        migrations.DeleteModel(
            name='VideoUpload',
        ),
    ]

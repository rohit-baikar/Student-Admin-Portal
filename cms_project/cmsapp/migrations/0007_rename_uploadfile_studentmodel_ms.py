# Generated by Django 5.0.1 on 2024-03-14 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0006_remove_studentmodel_upload_file_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentmodel',
            old_name='uploadfile',
            new_name='ms',
        ),
    ]

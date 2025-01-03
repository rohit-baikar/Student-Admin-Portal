# Generated by Django 5.0.1 on 2024-03-14 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0002_studentmodel_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='upload_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]

# Generated by Django 5.0.1 on 2024-03-14 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.6 on 2023-02-23 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Image', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='userEmail',
            new_name='email',
        ),
    ]

# Generated by Django 4.1.6 on 2023-02-23 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_user_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
    ]

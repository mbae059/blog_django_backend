# Generated by Django 4.1.6 on 2023-02-23 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Feed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_id', models.IntegerField(default=0)),
                ('email', models.EmailField(default='a@google.com', max_length=254)),
                ('content', models.TextField(default='')),
            ],
            options={
                'db_table': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_id', models.IntegerField(default=0)),
                ('email', models.EmailField(default='a@google.com', max_length=254)),
                ('is_like', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Like',
            },
        ),
        migrations.AddField(
            model_name='feed',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='feed',
            name='title',
            field=models.TextField(default='Title'),
        ),
    ]

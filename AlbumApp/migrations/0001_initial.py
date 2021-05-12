# Generated by Django 3.2.2 on 2021-05-12 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('AlbumId', models.AutoField(primary_key=True, serialize=False)),
                ('AlbumName', models.CharField(max_length=25)),
                ('Group', models.CharField(max_length=25)),
                ('DateAdded', models.DateField()),
                ('PhotoFileName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('GroupId', models.AutoField(primary_key=True, serialize=False)),
                ('GroupName', models.CharField(max_length=20)),
                ('PhotoFileName', models.CharField(max_length=100)),
            ],
        ),
    ]
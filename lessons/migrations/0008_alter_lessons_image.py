# Generated by Django 4.1.5 on 2023-03-01 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0007_alter_lessons_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='image',
            field=models.FilePathField(path='static/'),
        ),
    ]
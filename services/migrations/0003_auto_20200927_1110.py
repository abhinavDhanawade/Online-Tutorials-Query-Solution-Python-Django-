# Generated by Django 3.0.3 on 2020-09-27 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_tutorial_imagefile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='querysolution',
            name='post',
        ),
        migrations.RemoveField(
            model_name='querysolution',
            name='user',
        ),
        migrations.DeleteModel(
            name='QueryQuestion',
        ),
        migrations.DeleteModel(
            name='QuerySolution',
        ),
    ]

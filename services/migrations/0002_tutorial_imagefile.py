# Generated by Django 3.0.3 on 2020-09-26 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='imagefile',
            field=models.ImageField(default='', upload_to='services/images'),
        ),
    ]
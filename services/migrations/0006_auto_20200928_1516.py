# Generated by Django 3.0.3 on 2020-09-28 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_purchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='id',
        ),
        migrations.AddField(
            model_name='purchase',
            name='Referrence_Number',
            field=models.CharField(blank=True, default='8696802069', editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='fullname',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
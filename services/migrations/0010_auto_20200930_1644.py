# Generated by Django 3.0.3 on 2020-09-30 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_auto_20200930_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='Referrence_Number',
            field=models.CharField(blank=True, default='1966854574', editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]

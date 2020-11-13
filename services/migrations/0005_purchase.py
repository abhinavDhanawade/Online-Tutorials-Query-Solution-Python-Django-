# Generated by Django 3.0.3 on 2020-09-27 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0004_tutorial_approval'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchasedate', models.DateTimeField(default=django.utils.timezone.now)),
                ('customuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tuto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Tutorial')),
            ],
        ),
    ]

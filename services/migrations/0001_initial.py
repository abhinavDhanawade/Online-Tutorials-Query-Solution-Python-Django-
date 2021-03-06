# Generated by Django 3.0.3 on 2020-09-26 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=10)),
                ('email_ad', models.EmailField(default='NULL', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='QueryQuestion',
            fields=[
                ('title', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('example', models.TextField(default='')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('catego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('desc', models.TextField()),
                ('videofile', models.FileField(null=True, upload_to='services/videos')),
                ('price', models.IntegerField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('catego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Category')),
            ],
        ),
        migrations.CreateModel(
            name='QuerySolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.QueryQuestion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

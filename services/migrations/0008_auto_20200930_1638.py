# Generated by Django 3.0.3 on 2020-09-30 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_auto_20200929_1058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('image', models.ImageField(default='services/images/default.jpg', upload_to='services/profile_pics')),
                ('profession', models.CharField(max_length=200)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='purchase',
            name='Referrence_Number',
            field=models.CharField(blank=True, default='2128728945', editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
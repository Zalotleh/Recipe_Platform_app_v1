# Generated by Django 4.1 on 2022-08-16 21:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=200)),
                ('ingredients', models.TextField(max_length=500)),
                ('number_of_portions', models.CharField(max_length=100)),
                ('preparation_time', models.CharField(max_length=30)),
                ('total_time', models.CharField(max_length=30)),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('video', models.FileField(upload_to='')),
            ],
        ),
    ]
# Generated by Django 4.1 on 2022-08-18 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='video',
            field=models.FileField(upload_to='videos/'),
        ),
    ]
# Generated by Django 4.1 on 2022-09-09 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0006_alter_recipe_options_alter_recipe_external_video_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.CharField(blank=True, choices=[('Breakfast', 'Breakfast'), ('Dinner', 'Dinner'), ('Side Dish', 'Side Dish'), ('Vegeterian', 'Vegeterian'), ('Pizza', 'Pizza')], default='Other', max_length=30, null=True),
        ),
    ]
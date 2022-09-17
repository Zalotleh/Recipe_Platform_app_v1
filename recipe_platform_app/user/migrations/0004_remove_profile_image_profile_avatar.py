# Generated by Django 4.1 on 2022-08-26 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_profile_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="image",
        ),
        migrations.AddField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(default="bunny.jpg", upload_to="profile-pics"),
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-27 06:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PrivacySettings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("follower_can_see_email", models.BooleanField(default=False)),
                ("follower_can_see_bio", models.BooleanField(default=True)),
                ("follower_can_see_posts", models.BooleanField(default=True)),
                ("follower_can_see_following_list", models.BooleanField(default=True)),
                ("follower_can_see_follower_list", models.BooleanField(default=True)),
                ("following_can_see_email", models.BooleanField(default=False)),
                ("following_can_see_bio", models.BooleanField(default=True)),
                ("following_can_see_posts", models.BooleanField(default=True)),
                ("following_can_see_following_list", models.BooleanField(default=True)),
                ("following_can_see_follower_list", models.BooleanField(default=True)),
                ("others_can_see_email", models.BooleanField(default=False)),
                ("others_can_see_bio", models.BooleanField(default=True)),
                ("others_can_see_posts", models.BooleanField(default=True)),
                ("others_can_see_following_list", models.BooleanField(default=False)),
                ("others_can_see_follower_list", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="privacy_settings",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

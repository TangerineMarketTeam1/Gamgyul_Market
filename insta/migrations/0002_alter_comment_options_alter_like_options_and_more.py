# Generated by Django 5.0.8 on 2024-10-07 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("insta", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["created_at"]},
        ),
        migrations.AlterModelOptions(
            name="like",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="postimage",
            options={"ordering": ["post"]},
        ),
        migrations.AlterField(
            model_name="postimage",
            name="image",
            field=models.ImageField(upload_to="insta/"),
        ),
    ]

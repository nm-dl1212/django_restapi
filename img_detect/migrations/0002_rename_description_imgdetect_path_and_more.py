# Generated by Django 5.0.1 on 2024-01-14 08:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("img_detect", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="imgdetect",
            old_name="description",
            new_name="path",
        ),
        migrations.RenameField(
            model_name="imgdetect",
            old_name="name",
            new_name="title",
        ),
        migrations.RemoveField(
            model_name="imgdetect",
            name="price",
        ),
        migrations.RemoveField(
            model_name="imgdetect",
            name="review",
        ),
    ]
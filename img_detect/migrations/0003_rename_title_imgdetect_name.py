# Generated by Django 5.0.1 on 2024-01-14 08:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("img_detect", "0002_rename_description_imgdetect_path_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="imgdetect",
            old_name="title",
            new_name="name",
        ),
    ]

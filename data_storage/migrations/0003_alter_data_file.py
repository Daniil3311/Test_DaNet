# Generated by Django 5.1.1 on 2024-09-10 17:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data_storage", "0002_alter_data_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="data",
            name="file",
            field=models.FileField(upload_to="", verbose_name="file"),
        ),
    ]

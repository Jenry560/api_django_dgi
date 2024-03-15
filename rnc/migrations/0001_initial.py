# Generated by Django 5.0.3 on 2024-03-14 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DrRnc",
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
                ("rnc", models.FloatField()),
                ("nombre", models.CharField(max_length=255, null=True)),
                ("ocupacion", models.CharField(max_length=255, null=True)),
                ("status", models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
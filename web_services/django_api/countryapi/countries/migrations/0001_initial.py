# Generated by Django 4.2.11 on 2024-03-26 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Country",
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
                ("name", models.CharField(max_length=100)),
                ("capital", models.CharField(max_length=100)),
                ("area", models.IntegerField(help_text="(in square kilometers)")),
            ],
        ),
    ]

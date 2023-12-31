# Generated by Django 4.2.4 on 2023-08-30 07:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Wish",
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
                ("text", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="WishesInformation",
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
                ("name", models.CharField(max_length=255)),
                ("author_name", models.CharField(max_length=255)),
                ("occasion", models.CharField(max_length=255)),
                ("interests", models.CharField(max_length=255)),
                (
                    "style",
                    models.CharField(
                        choices=[
                            ("official", "official"),
                            ("fun", "fun"),
                            ("friendly", "friendly"),
                            ("informal", "informal"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "wishes_format",
                    models.CharField(
                        choices=[
                            ("greeting", "greeting"),
                            ("poem", "poem"),
                            ("joke", "joke"),
                        ],
                        max_length=50,
                    ),
                ),
                ("connection_kind", models.CharField(max_length=255)),
            ],
        ),
    ]

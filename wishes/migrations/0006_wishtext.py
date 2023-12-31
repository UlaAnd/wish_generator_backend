# Generated by Django 4.2.4 on 2023-09-05 09:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wishes", "0005_delete_wish_delete_wishmodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="WishText",
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
                (
                    "info",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wishes.wishesinformation",
                    ),
                ),
            ],
        ),
    ]

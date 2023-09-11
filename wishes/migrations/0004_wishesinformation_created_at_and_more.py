# Generated by Django 4.2.4 on 2023-09-04 11:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wishes", "0003_wishmodel_remove_wishesinformation_created_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="wishesinformation",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="wishesinformation",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]

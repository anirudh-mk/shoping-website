# Generated by Django 5.0.7 on 2024-07-30 16:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("website", "0004_delete_users"),
    ]

    operations = [
        migrations.CreateModel(
            name="Products",
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
                ("name", models.CharField(max_length=300)),
                ("price", models.IntegerField()),
                ("image", models.ImageField(upload_to="images")),
                ("is_new", models.BooleanField(default=False)),
                ("is_sale", models.BooleanField(default=False)),
            ],
        ),
    ]

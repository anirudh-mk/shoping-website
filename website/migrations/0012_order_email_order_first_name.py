# Generated by Django 5.0.7 on 2024-08-07 06:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0011_alter_usercart_total_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="email",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="first_name",
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]

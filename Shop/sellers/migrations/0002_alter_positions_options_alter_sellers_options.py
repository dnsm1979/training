# Generated by Django 5.0.2 on 2024-04-22 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sellers", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="positions",
            options={
                "verbose_name": "Позиция в фирме",
                "verbose_name_plural": "Позиции в фирме",
            },
        ),
        migrations.AlterModelOptions(
            name="sellers",
            options={"verbose_name": "Продавец", "verbose_name_plural": "Продавцы"},
        ),
    ]
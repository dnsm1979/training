# Generated by Django 5.0.2 on 2024-04-17 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="price",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="Стоимость"
            ),
        ),
        migrations.AlterField(
            model_name="products",
            name="quantity",
            field=models.IntegerField(verbose_name="Количество"),
        ),
    ]

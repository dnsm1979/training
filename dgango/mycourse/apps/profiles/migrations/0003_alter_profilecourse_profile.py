# Generated by Django 5.0.2 on 2024-07-03 15:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0002_profilecourse"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profilecourse",
            name="profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="profile_courses",
                to="profiles.profile",
            ),
        ),
    ]

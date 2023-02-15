# Generated by Django 4.1.5 on 2023-02-12 13:40

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="username",
            field=models.CharField(
                error_messages={"unique": "A user with that username already exists."},
                help_text="Required. 150 characters or fewer. ASCII letters and digits only.",
                max_length=150,
                unique=True,
                validators=[django.contrib.auth.validators.ASCIIUsernameValidator()],
                verbose_name="username",
            ),
        ),
    ]

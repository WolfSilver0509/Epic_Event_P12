# Generated by Django 4.2.2 on 2023-06-06 14:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentification", "0003_alter_user_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=105, unique=True),
        ),
    ]

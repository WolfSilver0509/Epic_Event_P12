# Generated by Django 4.2.2 on 2023-06-06 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0004_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]

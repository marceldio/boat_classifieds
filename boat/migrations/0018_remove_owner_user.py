# Generated by Django 4.2 on 2024-08-24 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boat', '0017_alter_owner_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='user',
        ),
    ]

# Generated by Django 5.0.7 on 2024-08-11 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boat', '0003_boat_description_boat_image_alter_boat_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='price',
            field=models.IntegerField(blank=True, default=None, help_text='Введите цену', null=True, verbose_name='цена'),
        ),
    ]
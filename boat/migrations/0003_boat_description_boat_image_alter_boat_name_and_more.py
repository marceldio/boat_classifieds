# Generated by Django 5.0.7 on 2024-08-11 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boat', '0002_boat_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='boat',
            name='description',
            field=models.TextField(blank=True, help_text='Введите описание товара', null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='boat',
            name='image',
            field=models.ImageField(blank=True, help_text='Загрузите изображение', null=True, upload_to='boat/photo', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='boat',
            name='name',
            field=models.CharField(help_text='Введите название лодки', max_length=50, verbose_name='названиe'),
        ),
        migrations.AlterField(
            model_name='boat',
            name='year',
            field=models.PositiveIntegerField(blank=True, help_text='Введите год выпуска лодки', null=True, verbose_name='год выпуска'),
        ),
    ]
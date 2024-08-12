# Generated by Django 5.0.7 on 2024-08-08 15:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boat', '0002_boat_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='имя')),
                ('email', models.EmailField(max_length=150, verbose_name='электронная почта')),
                ('message', models.TextField(verbose_name='сообщение')),
                ('closed', models.BooleanField(default=False, verbose_name='закрыт')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('boat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boat.boat', verbose_name='лодка')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
                'ordering': ['-created'],
            },
        ),
    ]

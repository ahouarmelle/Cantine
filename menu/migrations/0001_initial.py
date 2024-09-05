# Generated by Django 5.1.1 on 2024-09-05 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('creation_date', models.DateTimeField()),
                ('plat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='plat.platmodel')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
            },
        ),
    ]

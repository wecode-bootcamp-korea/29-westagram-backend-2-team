# Generated by Django 4.0.1 on 2022-01-14 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('emaail', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=120, unique=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]

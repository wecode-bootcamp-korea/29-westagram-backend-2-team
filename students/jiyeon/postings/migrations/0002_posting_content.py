# Generated by Django 4.0.1 on 2022-01-19 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='content',
            field=models.CharField(default='null', max_length=1000),
            preserve_default=False,
        ),
    ]

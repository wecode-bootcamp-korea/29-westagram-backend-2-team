# Generated by Django 4.0.1 on 2022-01-21 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0002_posting_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-22 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_channelinfo_subscribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoinfo',
            name='keyword',
            field=models.TextField(blank=True),
        ),
    ]

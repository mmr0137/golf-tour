# Generated by Django 3.0.5 on 2020-04-15 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golfer', '0002_golfer_managed_change'),
    ]

    operations = [
        migrations.AddField(
            model_name='golfer',
            name='golfer_city',
            field=models.TextField(blank=True, default='unknown'),
        ),
    ]

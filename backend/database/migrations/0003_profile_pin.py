# Generated by Django 2.2.5 on 2019-09-21 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20190921_0122'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pin',
            field=models.TextField(null=True),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-05 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='activated',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]

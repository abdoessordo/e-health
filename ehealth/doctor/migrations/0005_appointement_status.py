# Generated by Django 4.0.3 on 2022-05-01 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_alter_appointement_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointement',
            name='status',
            field=models.BooleanField(default=0),
        ),
    ]

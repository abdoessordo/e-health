# Generated by Django 4.0.3 on 2022-04-28 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visite',
            name='medcin_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visites', to='doctor.doctor'),
        ),
    ]
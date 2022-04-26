# Generated by Django 4.0.3 on 2022-04-25 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
        ('doctor', '0002_alter_visite_medcin_id_alter_visite_patient_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visite',
            name='patient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visites', to='patient.patient'),
        ),
    ]
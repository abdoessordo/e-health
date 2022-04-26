# Generated by Django 4.0.3 on 2022-04-25 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_alter_visite_patient_id'),
        ('patient', '0001_initial'),
        ('mutuelle', '0002_rename_all_mutuelle_allmutuelle'),
    ]

    operations = [
        migrations.AddField(
            model_name='allmutuelle',
            name='visite_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='doctor.visite'),
        ),
        migrations.AlterField(
            model_name='allmutuelle',
            name='patient_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
        ),
    ]
# Generated by Django 4.0.3 on 2022-04-24 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0001_initial'),
        ('landing', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('ville', models.CharField(max_length=250)),
                ('INP', models.IntegerField(primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('activated', models.BooleanField(default=0)),
                ('person_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='landing.person')),
            ],
        ),
        migrations.CreateModel(
            name='Visite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('medcin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visites', to='patient.patient')),
            ],
        ),
    ]

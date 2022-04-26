# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Meds(models.Model):
    code = models.IntegerField(db_column='CODE', primary_key=True)  # Field name made lowercase.
    nom = models.TextField(db_column='NOM', blank=True, null=True)  # Field name made lowercase.
    dci1 = models.TextField(db_column='DCI1', blank=True, null=True)  # Field name made lowercase.
    dosage1 = models.TextField(db_column='DOSAGE1', blank=True, null=True)  # Field name made lowercase.
    unite_dosage1 = models.TextField(db_column='UNITE_DOSAGE1', blank=True, null=True)  # Field name made lowercase.
    forme = models.TextField(db_column='FORME', blank=True, null=True)  # Field name made lowercase.
    presentation = models.TextField(db_column='PRESENTATION', blank=True, null=True)  # Field name made lowercase.
    ppv = models.FloatField(db_column='PPV', blank=True, null=True)  # Field name made lowercase.
    ph = models.FloatField(db_column='PH', blank=True, null=True)  # Field name made lowercase.
    prix_br = models.FloatField(db_column='PRIX_BR', blank=True, null=True)  # Field name made lowercase.
    princeps_generique = models.TextField(db_column='PRINCEPS_GENERIQUE', blank=True, null=True)  # Field name made lowercase.
    taux_remboursement = models.TextField(db_column='TAUX_REMBOURSEMENT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        pass

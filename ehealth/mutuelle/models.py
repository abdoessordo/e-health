from django.db import models
from requests import delete
from patient.models import Patient
from doctor.models import Visite


class AllMutuelle(models.Model):

    MUTUELLE_STATUS_PENDING = 'P'
    MUTUELLE_STATUS_COMPLETE = 'C'
    MUTUELLE_STATUS_CHOICES = [
        (MUTUELLE_STATUS_PENDING, 'Pending'),
        (MUTUELLE_STATUS_COMPLETE, 'Complete'),
    ]

    patient_id = models.ForeignKey(
        Patient, on_delete=models.CASCADE, null=False, default=0)
    visite_id = models.ForeignKey(
        Visite, on_delete=models.CASCADE, null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    mutuelle_status = models.CharField(
        max_length=1, choices=MUTUELLE_STATUS_CHOICES, default=MUTUELLE_STATUS_PENDING)
    total = models.DecimalField(max_digits=7, decimal_places=2)

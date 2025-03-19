from django.db import models
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse

class CertificateInstanceStatusChoices(ChoiceSet):
    """Certificate Instance State"""
    key = 'CertificateInstance.status'

    DEFAULT_VALUE = "planned"

    CHOICES = [
        ("active", "Active", "green"),
        ("planned", "Planned", "blue"),
        ("issued", "Issued", "orange"),
        ("expired", "Expired", "red")
    ]

class CertificateInstance(NetBoxModel):
    ca_reference = models.CharField(max_length=100, primary_key=True, verbose_name="CA Order Number")
    cert_reference = models.ForeignKey(
        to=Certificate,
        on_delete=models.PROTECT,
        related_name='certificate'
    )
    serial_number = models.CharField(
        max_length=100,
        unique=True
        )
    issue_date = models.DateField(
        blank=True, null=True, verbose_name="Not valid before"
    )
    expiry_date = models.DateField(
        blank=True, null=True, verbose_name="Expiration date"
    )
    status = models.CharField(
        max_length=32,
        default=CertificateInstanceStatusChoices.DEFAULT_VALUE,
        blank=False,
        verbose_name="Installation Status",
    )
    csr = models.TextField (
        max_length=32000,
        null=True,
        blank=True,
        verbose_name="Certificate CSR",
    )
    key = models.TextField (
        max_length=32000,
        null=True,
        blank=True,
        verbose_name="Certificate key",
    )
    pem = models.TextField (
        max_length=32000,
        null=True,
        blank=True,
        verbose_name="Certificate PEM",
    )

    # Colour choices
    def get_status_color(self):
        return CertificateInstanceStatusChoices.colors.get(self.status)
    
    class Meta:
        """Meta class"""

        ordering = ('ca_reference',)

    def __str__(self):
        return self.ca_reference
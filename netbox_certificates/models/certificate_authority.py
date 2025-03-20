from django.db import models
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse

class CertificateAuthorityStatusChoice(ChoiceSet):
    """CertificateAuthority Statuses"""
    key = 'CertificateAuthority.status'

    DEFAULT_VALUE = "planned"

    CHOICES = [
        ("active", "Active", "green"),
        ("planned", "Planned", "blue"),
        ("retired", "Retired", "red")
    ]


class CertificateAuthority(NetBoxModel):
    name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Certificate Authority Name",
        unique=True,
        help_text="Certificate Authority Name"
    )
    acme_url = models.URLField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name="ACME URL"
    )
    admin_url = models.URLField(
        max_length=256,
        null=False,
        blank=False,
        verbose_name="Administrative URL"
    )
    status = models.CharField(
        max_length=32,
        default=CertificateAuthorityStatusChoice.DEFAULT_VALUE,
        blank=False,
        verbose_name="Certificate Authority Status"
    )
    comments = models.TextField(
        blank=True
    )
    
    class Meta():
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """override"""
        return reverse("plugins:netbox_certificates:certificate_authority", args=[self.pk])
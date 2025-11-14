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
        verbose_name="Certificate Authority",
        unique=True,
        help_text="Certificate Authority Name"
    )
    org_id = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Certificate Organisation ID",
        help_text="The organisation ID assigned by the CA"
    )
    cert_profile_ev_id = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Certificate Profile ID (EV)",
        help_text="The CA certificate profile ID for EV certificates"
    )
    cert_profile_ov_id = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Certificate Profile ID (OV)",
        help_text="The CA certificate profile ID for OV certificates"
    )
    cert_profile_wildcard_id = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Certificate Profile ID (Wildcard OV)",
        help_text="The CA certificate profile ID for Wildcard OV certificates"
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
        verbose_name="Certificate Authority Status",
        choices=CertificateAuthorityStatusChoice
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
        return reverse("plugins:netbox_certificates:certificateauthority", args=[self.pk])
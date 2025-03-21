from django.db import models
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse

# Choices - extendable by key in configuration
class CertificateStatusChoices(ChoiceSet):
    """Certificate Statuses"""
    key = 'Certificate.status'

    DEFAULT_VALUE = "planned"

    CHOICES = [
        ("active", "Active", "green"),
        ("planned", "Planned", "blue"),
        ("issued", "Issued", "orange"),
        ("retired", "Retired", "red")
    ]

class CertificateTypeChoices(ChoiceSet):
    """Certificate Type"""
    key = 'Certificate.type'

    DEFAULT_VALUE = "ev"

    CHOICES = [
        ("ev", "Extended Validation", "green"),
        ("ov", "Organisation Validated", "blue"),
        ("evanchor", "EV Anchor", "purple"),
        ("other", "Other", "red")
    ]


# Need a choice here for type of certificate install
# e.g. single pem, pem with certs, jks, etc.
class CertificateInstallChoices(ChoiceSet):
    """Certificate Installation Type"""
    key = 'Certificate.install_type'

    DEFAULT_VALUE = "pem"

    CHOICES = [
        ("pem", "PEM with certificates after", "green"),
        ("pem_co", "PEM, Certificate Only", "blue"),
        ("jks", "Java Key Store", "purple"),
        ("pfx", "Windows, PFX", "red")
    ]

class Certificate(NetBoxModel):
    """Certificate definition class"""

    cn = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Common Name",
        unique=True,
        help_text="Unique Common Name"
    )
    # Could this point to a DNS record?
    san = ArrayField(
        base_field=models.CharField(max_length=256),
        null=True,
        blank=True,
        verbose_name="Subject Alternative Names",
        help_text="Comma separated list of fqdns to add into the CSR.",
    )
    device = models.ManyToManyField(
        to='dcim.Device',
        blank=True,
        verbose_name='Device',
        help_text='Device(s) with certificate installed'
    )
    ca = models.ManyToManyField(
        to="CertificateAuthority",
        verbose_name='Certificate Authority',
        related_name='certificates'
    )
    status = models.CharField(
        max_length=32,
        default=CertificateStatusChoices.DEFAULT_VALUE,
        blank=False,
        verbose_name="Certificate Status",
        choices=CertificateStatusChoices
    )
    type = models.CharField(
        max_length=32,
        default=CertificateTypeChoices.DEFAULT_VALUE,
        blank=False,
        verbose_name="Certificate Type",
        choices=CertificateTypeChoices
    )
    content = models.TextField (
        max_length=32000,
        null=True,
        blank=True,
        verbose_name="PEM Certificate"
    )
    vault_url = models.URLField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name="URL to corresponding vault",
    )
    fs_cert_location = models.TextField (
        max_length=300,
        null=True,
        blank=True,
        verbose_name="Location of cert Server Filesystem",
    )
    fs_key_location = models.TextField (
        max_length=300,
        null=True,
        blank=True,
        verbose_name="Location on Server Filesystem",
    )
    install_type = models.CharField(
        max_length=32,
        default=CertificateInstallChoices.DEFAULT_VALUE,
        blank=False,
        verbose_name="Certificate Installation Type",
        choices=CertificateInstallChoices
    )
    service_commands = models.TextField (
        max_length=32000,
        null=True,
        blank=True,
        verbose_name="Commands to run to restart service after a certificate change"
    )
    service_check = models.TextField (
        max_length=300,
        null=True,
        blank=True,
        verbose_name="Service Check Command",
        help_text=("This is the command the monitoring will run to pull a certificate from a device for this service.")
    )
    service_lb = models.BooleanField(
        verbose_name="via Loadbalancer?",
        default=False,
        null=True
    )
    comments = models.TextField(
        blank=True
    )
    # Need a field here for Service when it becomes available

    
    # Colour methods

    def get_status_color(self):
        return CertificateStatusChoices.colors.get(self.status)
    
    def get_type_color(self):
        return CertificateTypeChoices.colors.get(self.type)

    def get_install_type_color(self):
        return CertificateInstallChoices.colors.get(self.install_type)

    class Meta:
        """Meta class"""

        ordering = ('cn',)

    def __str__(self):
        return str(self.cn)

    def get_absolute_url(self):
        """override"""
        return reverse("plugins:netbox_certificates:certificate", args=[self.pk])

    def generate_csr(self):
        # Logic to generate CSR
        pass
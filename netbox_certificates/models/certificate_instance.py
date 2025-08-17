from django.db import models
from netbox.models import NetBoxModel
from netbox.models.features import ContactsMixin
from utilities.choices import ChoiceSet
from django.urls import reverse

from netbox_certificates.models import Certificate, CertificateAuthority

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
    ca_reference = models.CharField(
        max_length=100, 
        verbose_name="CA Order Number"
    )
    ca = models.ForeignKey(
        to=CertificateAuthority,
        on_delete=models.PROTECT,
        related_name='certificates',
        verbose_name='Certificate Authority',
        null=True
    )
    issuer = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )
    pubkey_algorithm = models.CharField(
        null=True,
        blank=True,
        max_length=100
    )
    pubkey_size = models.CharField(
        null=True,
        blank=True,
        max_length=100
    )
    pubkey_sha1 = models.CharField(
        null=True,
        blank=True,
        max_length=100
    )
    term = models.IntegerField(
        null=True,
        blank=True,
    )
    certificate = models.ForeignKey(
        to=Certificate,
        on_delete=models.CASCADE,
        related_name='instances',
        null=True
    )
    certificate_active = models.OneToOneField(
        to=Certificate,
        related_name='active',
        on_delete=models.CASCADE,
        null=True
    )
    certificate_latest = models.OneToOneField(
        to=Certificate,
        related_name='latest',
        on_delete=models.CASCADE,
        null=True
    )
    serial_number = models.CharField(
        max_length=100,
        unique=True
        )
    issue_date = models.DateTimeField(
        blank=True, null=True, verbose_name="Not valid before"
    )
    expiry_date = models.DateTimeField(
        blank=True, null=True, verbose_name="Expiration date"
    )
    status = models.CharField(
        max_length=32,
        default=CertificateInstanceStatusChoices.DEFAULT_VALUE,
        blank=False,
        verbose_name="Installation Status",
        choices=CertificateInstanceStatusChoices
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
    infrastructure_installer = models.ManyToManyField(
        to='tenancy.Contact',
        blank=True,
        verbose_name='Infrastructure Installer',
        help_text='Who installed the certificate?',
        related_name="infrastructure_installer"
    )
    comments = models.TextField(
        blank=True
    )

    search_fields = (
        ('ca_reference', 100),
        ('serial_number', 100),
        ('comments', 5000),
    )

    # Colour choices
    def get_status_color(self):
        return CertificateInstanceStatusChoices.colors.get(self.status)
    
    @classmethod
    def update_instances(self):
        for cert in Certificate.objects.order_by('cn').filter(status="issued"):
            instances = CertificateInstance.objects.order_by('-expiry_date').filter(certificate__cn=cert.cn)
            cert.update(active = instances.filter(status='active'))
            cert.update(latest = instances.first())
    
    class Meta:
        """Meta class"""

        ordering = ('ca_reference',)

    def __str__(self):
        return self.ca_reference
    
    def get_absolute_url(self):
        """override"""

        self.update_instances()
        return reverse("plugins:netbox_certificates:certificateinstance", args=[self.pk])
from django.db import models
from netbox.models import NetBoxModel
from netbox.models.features import ContactsMixin
from utilities.choices import ChoiceSet
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

# A 'choice' to represent the term all certificate instances from this cert should have
class CertificateTermChoices(ChoiceSet):
    """Certificate Term"""
    key = 'Certificate.term'

    DEFAULT_VALUE = 365

    CHOICES = [
        (47, 47),
        (100, 100),
        (200, 200),
        (365, 365)
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
    san = models.CharField(
        max_length=512,
        null=True,
        blank=True,
        verbose_name="Subject Alternative Names",
        help_text="Comma separated list of FQDN(s) to add into the CSR",
    )
    term = models.IntegerField(
        choices=CertificateTermChoices,
        default=CertificateTermChoices.DEFAULT_VALUE,
        blank=False,
        verbose_name='Certificate Term (days)',
        help_text='Certificate validity period (days)'
    )

    active = models.OneToOneField(
        to=CertificateInstance,
        on_delete=models.CASCADE,
    )

    latest = models.OneToOneField(
        to=CertificateInstance,
        on_delete=models.CASCADE,
    )

    device = models.ManyToManyField(
        to='dcim.Device',
        blank=True,
        verbose_name='Device',
        help_text='Device(s) with certificate installed'
    )
    vm = models.ManyToManyField(
        to='virtualization.VirtualMachine',
        blank=True,
        verbose_name='Virtual Machine',
        help_text='VM(s) with certificate installed'
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
        help_text=("Is this certificate installed on multiple hosts behind a loadbalancer?")

    )
    automated = models.BooleanField(
        verbose_name="Automated?",
        default=False,
        help_text=("Is the installation of this certificate automated?")
    )
    technical_owner = models.ManyToManyField(
        to='tenancy.Contact',
        blank=True,
        verbose_name='Technical (product) Owner',
        help_text='Escalation point outside of Infrastructure, within IT Services',
        related_name="technical_contact"
    )

    technical_group = models.ManyToManyField(
        to='tenancy.ContactGroup',
        blank=True,
        verbose_name='Technical (product) Owner (Group)',
        help_text='Escalation point outside of Infrastructure, within IT Services',
        related_name="technical_owner"
    )

    business_contact = models.ManyToManyField(
        to='tenancy.Contact',
        blank=True,
        verbose_name='Business Contact',
        help_text='Contacts within the business (outside of IT Services)',
        related_name="business_contact"
    )

    business_group = models.ManyToManyField(
        to='tenancy.ContactGroup',
        blank=True,
        verbose_name='Business Owner (Group)',
        help_text='Escalation point outside in business',
        related_name="business_group"
    )

    infrastructure_contact = models.ManyToManyField(
        to='tenancy.Contact',
        blank=True,
        verbose_name='Infrastructure Contact',
        help_text='Escalation point within Infrastructure',
        related_name="infrastructure_contact"
    )

    infrastructure_group = models.ManyToManyField(
        to='tenancy.ContactGroup',
        blank=True,
        verbose_name='Infrastructure Owner (Group)',
        help_text='Escalation group within Infrastructure',
        related_name="infrastructure_group"
    )
    
    comments = models.TextField(
        blank=True
    )
    # Need a field here for Service when it becomes available

    @property
    def get_active(self):
        return self.instances.order_by('-expiry_date').filter(status="active").first()
    
    @property
    def get_latest(self):
        return self.instances.order_by('-expiry_date').first()
    
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
        self.active = get_active(self)
        self.latest = get_latest(self)
        return reverse("plugins:netbox_certificates:certificate", args=[self.pk])

    def generate_csr(self):
        # Logic to generate CSR
        pass

from netbox_certificates.models import CertificateInstance
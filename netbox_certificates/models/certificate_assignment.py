from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet

# Existing Certificate, CertificateInstance, etc., remain in place...

class CertificateAssignmentStatusChoices(ChoiceSet):
    """Certificate Assignment Installation Type"""
    key = "CertificateAssignment.status"

    DEFAULT_VALUE = "pending"
    STATUS_ACTIVE = 'active'

    CHOICES = [
            ("active", "Latest", "green"),
            ("pending", "Pending Deployment", "blue"),
            ("mismatch", "Needs Update", "orange"),
            ("error", "Unreachable", "black"),
            ("expired", "Expired", "red")
    ]

class CertificateInstallationMethodChoices(ChoiceSet):
    key = 'CertificateAssignment.installation_method'

    DEFAULT_VALUE = 'manual'

    CHOICES = [
        ('ansible', 'Ansible', 'green'),
        ('acme', 'ACME', 'green'),
        ('script-auto', 'Script - Automatic', 'green'),
        ('script-manual', 'Script - Manual', 'orange'),
        ('manual', 'Manual', 'red'),
        ('third-party', 'Third Party', 'purple'),
    ]

class CertificateAssignment(NetBoxModel):
    """
    Junction model mapping a logical Certificate to an IPAddress endpoint.
    """
    certificate = models.ForeignKey(
        to='Certificate',
        on_delete=models.CASCADE,
        related_name='assignments'
    )
    ip_address = models.ForeignKey(
        to='ipam.IPAddress',
        on_delete=models.CASCADE,
        related_name='certificate_assignments'
    )
    # New Link: Foreign Key to NetBox Core Service
    service = models.ForeignKey(
        to='ipam.Service',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='certificate_assignments',
        help_text='Associated application service'
    )
    installation_method = models.CharField(
        max_length=50,
        choices=CertificateInstallationMethodChoices,
        default=CertificateInstallationMethodChoices.DEFAULT_VALUE,
        help_text='Method used to deploy/install the certificate on the target'
    )
    port = models.PositiveIntegerField(
        default=443,
        help_text="TCP port where the certificate is served"
    )
    status = models.CharField(
        max_length=50,
        choices=CertificateAssignmentStatusChoices,
        default=CertificateAssignmentStatusChoices.DEFAULT_VALUE
    )
    installed_serial = models.CharField(
        max_length=100,
        blank=True,
        help_text="Serial number detected during live SSL probe"
    )
    last_verified = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('ip_address', 'port')
        unique_together = ('certificate', 'ip_address', 'port')

    def save(self, *args, **kwargs):
        # Optional: Auto-populate port from selected Service if port is default/blank
        if self.service and self.service.ports:
            # Take the primary port from the service definition
            self.port = self.service.ports[0]

        # Check if the assignment is being moved from an existing certificate
        old_cert = None
        if self.pk:
            original = CertificateAssignment.objects.filter(pk=self.pk).first()
            if original and original.certificate_id != self.certificate_id:
                old_cert = original.certificate

        super().save(*args, **kwargs)
        
        # Recalculate consistency on the associated certificate
        if self.certificate:
            self.certificate.update_host_consistency()

        # Update current certificate
        if self.certificate:
            self.certificate.update_host_consistency()

        # Update previous certificate if reassigned
        if old_cert:
            old_cert.update_host_consistency()

    def delete(self, *args, **kwargs):
        cert = self.certificate
        super().delete(*args, **kwargs)
        # Recalculate consistency after removing this assignment
        if cert:
            cert.update_host_consistency()

    def __str__(self):
        target = self.ip_address.dns_name or str(self.ip_address.address.ip)
        return f"{self.certificate.cn} -> {target}:{self.port}"

    def get_compliance_status(self):
        """
        Compares live installed_serial against the primary/latest active CertificateInstance.
        """
        # Grab latest active instance ordered by expiration / creation
        latest_instance = self.certificate.instances.order_by('-valid_to').first()
        if not latest_instance or not self.installed_serial:
            return 'pending'
        
        cleaned_installed = self.installed_serial.replace(':', '').lower()
        cleaned_latest = latest_instance.serial_number.replace(':', '').lower()
        
        if cleaned_installed == cleaned_latest:
            return 'active'
        return 'mismatch'

    def get_absolute_url(self):
        return reverse('plugins:netbox_certificates:certificateassignment', kwargs={'pk': self.pk})

    # Color methods for NetBox ChoiceFieldColumn badges
    def get_status_color(self):
        return CertificateAssignmentStatusChoices.colors.get(self.status)

    def get_installation_method_color(self):
        return CertificateInstallationMethodChoices.colors.get(self.installation_method)

    

from django.db import models
from netbox.models import NetBoxModel

# Existing Certificate, CertificateInstance, etc., remain in place...

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
    port = models.PositiveIntegerField(
        default=443,
        help_text="TCP port where the certificate is served"
    )
    status = models.CharField(
        max_length=50,
        default='pending',
        choices=[
            ('active', 'Active / In Sync'),
            ('pending', 'Pending Deployment'),
            ('mismatch', 'Outdated Instance Running'),
            ('error', 'Unreachable / Probe Failed'),
        ]
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
        super().save(*args, **kwargs)

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
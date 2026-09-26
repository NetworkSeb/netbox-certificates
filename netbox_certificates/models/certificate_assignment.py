from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet

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


class CertificateInstallationApplicationChoices(ChoiceSet):
    key = 'CertificateAssignment.installation_application'

    DEFAULT_VALUE = 'apache'

    CHOICES = [
        ('apache', 'Apache', 'green'),
        ('nginx', 'NGINX', 'green'),
        ('iis', 'Internet Information Services (IIS)', 'green'),
        ('exchange', 'Microsoft Exchange', 'green'),
        ('custom', 'Custom Application', 'orange'),
        ('other', 'Other', 'red'),
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

    installation_type = models.CharField(
        max_length=32,
        choices=CertificateInstallationMethodChoices,
        blank=True,
        null=True,
        verbose_name="Installation Type",
        help_text="Installation mechanism for this assignment (defaults to parent Certificate's installation type if blank)."
    )

    installation_application = models.CharField(
        max_length=50,
        choices=CertificateInstallationMethodChoices,
        default=CertificateInstallationMethodChoices.DEFAULT_VALUE,
        help_text='Application configured to use the certificat'
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

    def update_target_config_context(self, target=None):
        """
        Pushes certificate deployment metadata into the parent Device or VM's
        local_context_data dictionary under the 'certs' key.
        """
        # 1. Resolve parent Device or VirtualMachine from assigned_object
        if not target and self.ip_address and self.ip_address.assigned_object:
            assigned = self.ip_address.assigned_object
            target = getattr(assigned, 'device', None) or getattr(assigned, 'virtual_machine', None)

        if not target:
            return

        # 2. Safely resolve host interfaces (DCIM Interface vs Virtualization VMInterface)
        interfaces_rel = getattr(target, 'interfaces', None)
        if interfaces_rel is None:
            return

        interface_list = interfaces_rel.all() if hasattr(interfaces_rel, 'all') else interfaces_rel

        # 3. Collect all distinct assignments across host interfaces
        host_assignments = set()
        for iface in interface_list:
            if hasattr(iface, 'ip_addresses'):
                ip_qs = iface.ip_addresses.all() if hasattr(iface.ip_addresses, 'all') else iface.ip_addresses()
                for ip in ip_qs:
                    # Access reverse relation manager directly (do NOT call it)
                    if hasattr(ip, 'certificate_assignments'):
                        host_assignments.update(ip.certificate_assignments.all())

        # 4. Construct the "certs" data structure using Certificate.service_commands
        certs_list = []
        for assign in host_assignments:
            cert = assign.certificate
            raw_commands = getattr(cert, 'service_commands', '') or ''

            # Parse string or list into JSON array
            if isinstance(raw_commands, str):
                commands = [cmd.strip() for cmd in raw_commands.splitlines() if cmd.strip()]
            elif isinstance(raw_commands, list):
                commands = raw_commands
            else:
                commands = []

            certs_list.append({
                "cn": cert.cn,
                "commands": commands
            })

        # 5. Atomic update of local_context_data on Device / VM
        context = dict(target.local_context_data or {})
        
        if certs_list:
            context['certs'] = certs_list
        else:
            context.pop('certs', None)

        target.local_context_data = context
        target.save(update_fields=['local_context_data'])

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

        # Default installation_type from parent Certificate on creation or if left blank
        if not self.installation_type and self.certificate:
            if hasattr(self.certificate, 'installation_type'):
                self.installation_type = self.certificate.installation_type

        super().save(*args, **kwargs)
        self.update_target_config_context()
        
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

        target = None
        if self.ip_address and self.ip_address.assigned_object:
            assigned = self.ip_address.assigned_object
            target = getattr(assigned, 'device', None) or getattr(assigned, 'virtual_machine', None)

        super().delete(*args, **kwargs)

        # Recalculate consistency after removing this assignment
        if cert:
            cert.update_host_consistency()

        if target:
            self.update_target_config_context(target=target)

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

    
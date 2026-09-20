from netbox.plugins import PluginTemplateExtension
from django.contrib.contenttypes.models import ContentType
from django_tables2 import RequestConfig
from ipam.models import IPAddress
from dcim.models import Device
from virtualization.models import VirtualMachine
from .models import CertificateAssignment
from .tables import CertificateAssignmentTable


class DeviceCertificateAssignmentsExtension(PluginTemplateExtension):
    models = ['dcim.device', 'virtualization.virtualmachine']

    def right_page(self):
        obj = self.context['object']
        
        # Collect IDs of all interfaces on this Device or VM
        interface_ids = obj.interfaces.values_list('id', flat=True)
        
        # Determine ContentType (dcim.interface vs virtualization.vminterface)
        if obj._meta.model_name == 'device':
            ct = ContentType.objects.get(app_label='dcim', model='interface')
        else:
            ct = ContentType.objects.get(app_label='virtualization', model='vminterface')

        # Find all IP addresses assigned to those interfaces
        ip_ids = IPAddress.objects.filter(
            assigned_object_type=ct,
            assigned_object_id__in=interface_ids
        ).values_list('id', flat=True)

        # Query all certificate assignments for these IPs
        assignments = CertificateAssignment.objects.filter(
            ip_address_id__in=ip_ids
        ).select_related('certificate', 'ip_address')

        return self.render('netbox_certificates/inc/device_certificates.html', {
            'assignments': assignments,
        })

template_extensions = [DeviceCertificateAssignmentsExtension]

class IPAddressCertificateAssignments(PluginTemplateExtension):
    model = 'ipam.ipaddress'

    def right_page(self):
        obj = self.context.get('object')

        # Safety check: ensure object exists and is explicitly an IPAddress
        if not isinstance(obj, IPAddress):
            return ''

        # Retrieve assignments bound to this specific IP Address
        assignments = CertificateAssignment.objects.filter(ip_address=obj)
        
        if not assignments.exists():
            return ''

        # Instantiate table excluding redundant 'ip_address' and 'pk' columns
        table = CertificateAssignmentTable(
            assignments,
            exclude=('ip_address', 'pk')
        )
        RequestConfig(self.context['request']).configure(table)

        return self.render('netbox_certificates/inc/ipaddress_certificates.html', extra_context={
            'certificate_assignments_table': table,
            'assignments_count': assignments.count(),
        })


template_extensions = [IPAddressCertificateAssignments]

class HostCertificateAssignments(PluginTemplateExtension):
    model = 'ipam.ipaddress'

    def right_page(self):
        obj = self.context.get('object')

        # 1. Direct IPAddress page
        if isinstance(obj, IPAddress):
            assignments = CertificateAssignment.objects.filter(ip_address=obj)

        # 2. Device or VirtualMachine page
        elif isinstance(obj, (Device, VirtualMachine)):
            # Gather assignments across all IPs assigned to this host's interfaces
            interfaces = getattr(obj, 'interfaces', None)
            if not interfaces:
                return ''
            
            assignments = CertificateAssignment.objects.filter(
                ip_address__assigned_object_id__in=interfaces.values_list('id', flat=True)
            )
        else:
            return ''

        if not assignments.exists():
            return ''

        table = CertificateAssignmentTable(
            assignments,
            exclude=('pk',)
        )
        RequestConfig(self.context['request']).configure(table)

        return self.render('netbox_certificates/inc/ipaddress_certificates.html', extra_context={
            'certificate_assignments_table': table,
            'assignments_count': assignments.count(),
        })


template_extensions = [HostCertificateAssignments]

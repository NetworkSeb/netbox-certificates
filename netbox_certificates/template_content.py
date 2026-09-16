from netbox.plugins import PluginTemplateExtension
from django.contrib.contenttypes.models import ContentType
from django_tables2 import RequestConfig
from ipam.models import IPAddress
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
        # Retrieve all certificate assignments for this IPAddress object
        assignments = CertificateAssignment.objects.filter(ip_address=self.context['object'])
        
        if not assignments.exists():
            return ''

        # Render table excluding redundant IP Address and PK columns
        table = CertificateAssignmentTable(
            assignments,
            exclude=('ip_address', 'pk')
        )
        RequestConfig(self.context['request'], paginate={'per_page': 5}).configure(table)

        return self.render('netbox_certificates/inc/ipaddress_certificates.html', extra_context={
            'certificate_assignments_table': table,
            'assignments_count': assignments.count(),
        })


template_extensions = [IPAddressCertificateAssignments]
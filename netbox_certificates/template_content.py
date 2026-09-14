from netbox.plugins import PluginTemplateExtension
from django.contrib.contenttypes.models import ContentType
from ipam.models import IPAddress
from .models import CertificateAssignment

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
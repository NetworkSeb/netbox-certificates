import django_filters
from django.contrib.contenttypes.models import ContentType
from netbox.filtersets import NetBoxModelFilterSet
from ipam.models import IPAddress
from dcim.models import Device
from virtualization.models import VirtualMachine
from netbox_certificates.models import CertificateAssignment, Certificate

class CertificateAssignmentFilterSet(NetBoxModelFilterSet):
    device_id = django_filters.NumberFilter(method='filter_device')
    virtual_machine_id = django_filters.NumberFilter(method='filter_vm')
    ip_address_id = django_filters.ModelChoiceFilter(
        queryset=IPAddress.objects.all()
    )
    certificate_id = django_filters.ModelChoiceFilter(
        queryset=Certificate.objects.all()
    )

    class Meta:
        model = CertificateAssignment
        fields = ['id', 'certificate', 'ip_address', 'port', 'status']

    def filter_device(self, queryset, name, value):
        ct = ContentType.objects.get_for_model(Device)
        ip_ids = IPAddress.objects.filter(
            assigned_object_type=ct,
            assigned_object_id=value
        ).values_list('id', flat=True)
        return queryset.filter(ip_address_id__in=ip_ids)

    def filter_vm(self, queryset, name, value):
        ct = ContentType.objects.get_for_model(VirtualMachine)
        ip_ids = IPAddress.objects.filter(
            assigned_object_type=ct,
            assigned_object_id=value
        ).values_list('id', flat=True)
        return queryset.filter(ip_address_id__in=ip_ids)
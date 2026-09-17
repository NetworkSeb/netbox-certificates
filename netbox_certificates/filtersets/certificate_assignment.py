import django_filters
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from netbox.filtersets import NetBoxModelFilterSet
from ipam.models import IPAddress, Service
from dcim.models import Device
from virtualization.models import VirtualMachine
from netbox_certificates.models import CertificateAssignment, Certificate, CertificateAssignmentStatusChoices, CertificateInstallationMethodChoices

class CertificateAssignmentFilterSet(NetBoxModelFilterSet):
    device_id = django_filters.NumberFilter(method='filter_device')
    virtual_machine_id = django_filters.NumberFilter(method='filter_vm')
    certificate_id = filterset_mixin_all = None  # Standard NetBox mixin defaults

    certificate_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Certificate.objects.all(),
        label='Certificate (ID)',
    )
    ip_address_id = django_filters.ModelMultipleChoiceFilter(
        queryset=IPAddress.objects.all(),
        label='IP Address (ID)',
    )
    service_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Service.objects.all(),
        label='Service (ID)',
    )
    status = django_filters.MultipleChoiceFilter(
        choices=CertificateAssignmentStatusChoices,
    )
    installation_method = django_filters.MultipleChoiceFilter(
        choices=CertificateInstallationMethodChoices,
    )

    class Meta:
        model = CertificateAssignment
        fields = ('id', 'certificate', 'ip_address', 'service', 'port', 'status', 'installation_method')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset

        return queryset.filter(
            Q(certificate__cn__icontains=value) |
            Q(ip_address__address__icontains=value) |
            Q(ip_address__dns_name__icontains=value) |
            Q(service__name__icontains=value) |
            Q(installed_serial__icontains=value)
        ).distinct()

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
from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from netbox.api.fields import ChoiceField
from ipam.api.serializers import IPAddressSerializer, ServiceSerializer
from ipam.models import IPAddress, Service
from netbox_certificates.models import Certificate, CertificateAssignment, CertificateInstallationMethodChoices
from .certificate import CertificateSerializer

class NestedIPAddressWithDNSNameSerializer(IPAddressSerializer):
    """Custom nested IPAddress serializer to expose dns_name in brief mode."""
    class Meta(IPAddressSerializer.Meta):
        fields = ('id', 'url', 'display', 'address', 'dns_name', 'description')
        brief_fields = ('id', 'url', 'display', 'address', 'dns_name')


class CertificateAssignmentSerializer(NetBoxModelSerializer):
    # Use CertificateSerializer for full/brief representation
    certificate = CertificateSerializer(nested=True, read_only=True)
    certificate_id = serializers.PrimaryKeyRelatedField(
        queryset=Certificate.objects.all(),
        source='certificate',
        write_only=True
    )

    # Use the custom nested IP serializer to ensure dns_name is returned
    ip_address = NestedIPAddressWithDNSNameSerializer(nested=True, read_only=True)
    ip_address_id = serializers.PrimaryKeyRelatedField(
        queryset=IPAddress.objects.all(),
        source='ip_address',
        write_only=True
    )

    service = ServiceSerializer(nested=True, read_only=True, required=False, allow_null=True)
    service_id = serializers.PrimaryKeyRelatedField(
        queryset=Service.objects.all(),
        source='service',
        write_only=True,
        required=False,
        allow_null=True
    )

    installation_method = ChoiceField(
        choices=CertificateInstallationMethodChoices,
        required=False
    )

    class Meta:
        model = CertificateAssignment
        fields = [
            'id', 'url', 'display', 'certificate', 'certificate_id', 
            'ip_address', 'ip_address_id', 'service', 'service_id', 
            'port', 'status', 'installation_method', 'installed_serial', 'last_verified', 
            'created', 'last_updated'
        ]
        # Include custom fields in brief responses for assignment lists
        brief_fields = ('id', 'url', 'display', 'certificate', 'ip_address', 'port', 'status', 'installation_method')
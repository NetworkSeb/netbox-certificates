from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from ipam.api.serializers import IPAddressSerializer, ServiceSerializer
from ipam.models import IPAddress, Service
from netbox_certificates.models import Certificate, CertificateAssignment

class CertificateAssignmentSerializer(NetBoxModelSerializer):
    certificate = serializers.PrimaryKeyRelatedField(
        queryset=Certificate.objects.all()
    )
    ip_address = IPAddressSerializer(nested=True, read_only=True)
    ip_address_id = serializers.PrimaryKeyRelatedField(
        queryset=IPAddress.objects.all(),
        source='ip_address',
        write_only=True
    )
    # Nested Service Serializer (Read-Only) + Write-Only FK
    service = ServiceSerializer(nested=True, read_only=True, required=False, allow_null=True)
    service_id = serializers.PrimaryKeyRelatedField(
        queryset=Service.objects.all(),
        source='service',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = CertificateAssignment
        fields = [
            'id', 'url', 'display', 'certificate', 'ip_address', 'ip_address_id',
            'service', 'service_id', 'port', 'status', 'installed_serial',
            'last_verified', 'created', 'last_updated'
        ]
        brief_fields = ('id', 'url', 'display', 'port', 'status')
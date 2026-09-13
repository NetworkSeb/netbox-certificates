from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from ipam.api.serializers import IPAddressSerializer
from netbox_certificates.models import Certificate, CertificateAssignment

class CertificateAssignmentSerializer(NetBoxModelSerializer):
    certificate = serializers.PrimaryKeyRelatedField(
        queryset=Certificate.objects.all()
    )
    ip_address = IPAddressSerializer()

    class Meta:
        model = CertificateAssignment
        fields = [
            'id', 'certificate', 'ip_address', 'port', 
            'status', 'installed_serial', 'last_verified',
            'created', 'last_updated'
        ]
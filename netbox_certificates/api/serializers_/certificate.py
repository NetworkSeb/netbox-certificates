from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from dcim.api.serializers import DeviceSerializer

from netbox_certificates.models import Certificate
from netbox_certificates.api.nested_serializers import NestedCertificateAuthoritySerializer, NestedCertificateInstanceSerializer

class CertificateSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_certificates-api:certificate-detail'
    )

    instance_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Certificate
        ca = NestedCertificateAuthoritySerializer()
        device = DeviceSerializer(nested=True)
        instance = NestedCertificateInstanceSerializer()

        fields = (
            'id',
            'display',
            'custom_fields',
            'cn',
            'instance_count',
            'url',
            'san',
            'device',
            'status', 
            'type', 
            'install_type', 
            'fs_cert_location', 
            'fs_key_location', 
            'vault_url',
            'service_commands',
            'service_check',
            'service_lb',
            'ca',
            'content',
            'created',
            'last_updated',
            'comments',
            'tags'
        )
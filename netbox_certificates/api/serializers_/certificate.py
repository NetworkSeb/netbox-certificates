from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from dcim.api.serializers import DeviceSerializer
from tenancy.api.serializers import ContactSerializer, ContactGroupSerializer
from virtualization.api.serializers import VirtualMachineSerializer

from netbox_certificates.models import Certificate
from netbox_certificates.api.nested_serializers import NestedCertificateAuthoritySerializer, NestedCertificateInstanceSerializer

class CertificateSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_certificates-api:certificate-detail'
    )

    instance_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Certificate

        device = DeviceSerializer(nested=True, allow_null=True)
        vm = VirtualMachineSerializer(nested=True, allow_null=True)
        
        technical_owner = ContactSerializer(nested=True, allow_null=True)
        business_contact = ContactSerializer(nested=True, allow_null=True)
        infrastructure_contact = ContactSerializer(nested=True, allow_null=True)
        
        technical_group = ContactGroupSerializer(nested=True, allow_null=True)
        business_group = ContactGroupSerializer(nested=True, allow_null=True)
        infrastructure_group = ContactGroupSerializer(nested=True, allow_null=True)
        
        instance = NestedCertificateInstanceSerializer()
        active = NestedCertificateInstanceSerializer()
        latest = NestedCertificateInstanceSerializer()

        fields = (
            'id',
            'display',
            'custom_fields',
            'cn',
            'instance_count',
            'url',
            'san',
            'device',
            'vm',
            'status',
            'active',
            'latest',
            'type',
            'term',
            'install_type', 
            'fs_cert_location', 
            'fs_key_location', 
            'vault_url',
            'service_commands',
            'service_check',
            'monitor',
            'service_lb',
            'host_consistent',
            'automated',
            'technical_owner',
            'technical_group',
            'business_contact',
            'business_group',
            'infrastructure_contact',
            'infrastructure_group',
            'content',
            'created',
            'last_updated',
            'comments',
            'tags'
        )
        
        brief_fields = (
            'cn',
            'san',
            'status',
            'type',
            'term',
            'vm',
            'device'
        )
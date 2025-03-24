from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from dcim.api.serializers import NestedDeviceSerializer

from netbox_certificates.models import Certificate

class CertificateSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_certificates-api:certificate-detail'
    )

    instance_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Certificate
        ca = NestedCertificateAuthoritySerializer()
        device = NestedDeviceSerializer()
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

class NestedCertificateSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_certificates-api:certificate-detail'
    )

    class Meta:
        model = Certificate
        fields = (
            'id',
            'cn',
            'san'
        )

class CertificateInstanceSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_certificates-api:certificateinstance-detail'
    )

    class Meta:
        model = CertificateInstance
        certificate = NestedCertificateSerializer()
        ca = NestedCertificateAuthoritySerializer()

        fields = (
            'id',
            'display',
            'custom_fields',
            'url',
            'created',
            'last_updated',
            'pk',
            'certificate',
            'ca',
            'ca_reference',
            'serial_number',
            'issue_date',
            'expiry_date',
            'status'
            'csr',
            'key',
            'pem',
            'comments',
            'tags'
        )

class NestedCertificateInstanceSerializer(WritableNestedSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_certificates-api:certificateinstance-detail'
    )

    class Meta:
        model = CertificateInstance
        fields = (
            'id',
            'certificate',
            'ca'
        )

class CertificateAuthoritySerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_certificates-api:certificateauthority-detail'
    )

    certificate_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = CertificateAuthority

        fields = (
            'id',
            'display',
            'custom_fields',
            'url',
            'created',
            'certificate_count',
            'last_updated',
            'name',
            'acme_url',
            'admin_url',
            'status',
            'actions'
            'comments',
            'tags'
        )

class NestedCertificateAuthoritySerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_certificates-api:certificateauthority-detail'
    )

    class Meta:
        model = CertificateAuthority
        fields = (
            'id',
            'name'
        )        
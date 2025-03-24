from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer

from netbox_certificates.models import CertificateInstance
from netbox_certificates.api.serializers_ import NestedCertificateSerializer, NestedCertificateAuthoritySerializer

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
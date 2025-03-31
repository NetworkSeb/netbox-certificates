from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from tenancy.api.serializers import ContactSerializer

from netbox_certificates.models import CertificateInstance
from ..nested_serializers import NestedCertificateSerializer, NestedCertificateAuthoritySerializer

class CertificateInstanceSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_certificates-api:certificateinstance-detail'
    )

    class Meta:
        model = CertificateInstance
        certificate = NestedCertificateSerializer()
        ca = NestedCertificateAuthoritySerializer()
        infrastructure_installer = ContactSerializer(nested=True, allow_null=True)

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
            'status',
            'csr',
            'key',
            'pem',
            'issuer',
            'pubkey_algorithm',
            'pubkey_size',
            'pubkey_sha1',
            'term',
            'infrastructure_installer',
            'comments',
            'tags'
        )

        brief_fields = (
            'certificate',
            'status',
            'serial_number',
            'ca',
        )
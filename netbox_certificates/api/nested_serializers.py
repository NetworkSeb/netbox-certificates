from rest_framework import serializers
from netbox.api.serializers import WritableNestedSerializer

from netbox_certificates.models import Certificate, CertificateAuthority, CertificateInstance


__all__ = (
    "NestedCertificateAuthoritySerializer",
    "NestedCertificateInstanceSerializer",
    "NestedCertificateSerializer"
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
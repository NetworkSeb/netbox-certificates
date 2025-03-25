from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer

from netbox_certificates.models import CertificateAuthority

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
            'actions',
            'comments',
            'tags'
        )
from netbox.filtersets import NetBoxModelFilterSet

from netbox_certificates.models import CertificateAuthority

class CertificateAuthorityFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = CertificateAuthority
        fields = (
            'name',
            'acme_url',
            'admin_url',
            'status',
            'comments',
            'tags'
        )

    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)
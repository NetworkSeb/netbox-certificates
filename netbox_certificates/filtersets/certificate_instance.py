from netbox.filtersets import NetBoxModelFilterSet

from netbox_certificates.models import CertificateInstance

class CertificateInstanceFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = CertificateInstance
        fields = (
            'ca_reference',
            'certificate',
            'ca',
            'serial_number',
            'issue_date',
            'expiry_date',
            'status',
            'csr',
            'key',
            'pem',
            'comments',
            'tags'
        )

    def search(self, queryset, name, value):
        return queryset.filter(certificate__icontains=value)
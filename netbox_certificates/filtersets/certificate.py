from netbox.filtersets import NetBoxModelFilterSet

from netbox_certificates.models import Certificate

class CertificateFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Certificate
        fields = (
            'cn', 
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
            'comments',
            'tags'
        )

    def search(self, queryset, name, value):
        return queryset.filter(cn__icontains=value)
    
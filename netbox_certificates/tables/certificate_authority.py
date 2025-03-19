import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from netbox_certificates.models import CertificateAuthority

class CertificateInstanceTable(NetBoxTable):
    ca_reference = tables.Column(
        linkify=True
    )
    status = ChoiceFieldColumn()

    class Meta(NetBoxTable.Meta):
        model = CertificateAuthority
        fields = (
            'pk',
            'name',
            'acme_url',
            'admin_url',
            'status',
            'actions'
        )
        default_columns = (
            'name',
            'status'
        )
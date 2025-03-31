import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from netbox_certificates.models import CertificateInstance

class CertificateInstanceTable(NetBoxTable):
    ca_reference = tables.Column(
        linkify=True
    )
    status = ChoiceFieldColumn()

    class Meta(NetBoxTable.Meta):
        model = CertificateInstance
        fields = (
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
            'issuer',
            'pubkey_algorithm',
            'pubkey_size',
            'pubkey_sha1',
            'term',
            'actions'
        )
        default_columns = (
            'ca_reference',
            'certificate',
            'serial_number',
            'status',
            'issue_date',
            'expiry_date'
        )
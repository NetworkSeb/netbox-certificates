import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from netbox_certificates.models import CertificateAuthority

class CertificateAuthorityTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    status = ChoiceFieldColumn()
    certificate_count = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = CertificateAuthority
        fields = (
            'pk',
            'name',
            'org_id',
            'cert_profile_ev_id',
            'cert_profile_ov_id',
            'acme_url',
            'admin_url',
            'status',
            'actions'
        )
        default_columns = (
            'name',
            'status'
        )
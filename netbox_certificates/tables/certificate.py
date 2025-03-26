import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from netbox_certificates.models import Certificate

class CertificateTable(NetBoxTable):
    cn = tables.Column(
        linkify=True
    )
    status = ChoiceFieldColumn()
    type = ChoiceFieldColumn()
    install_type = ChoiceFieldColumn()
    instances = tables.Column()
    ca_id = tables.Column(
        linkify=True
    )
    instance_count = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = Certificate
        fields = (
            'pk',
            'id', 
            'cn', 
            'san', 
            'status',
            'device', 
            'type', 
            'install_type', 
            'fs_cert_location', 
            'fs_key_location', 
            'created',
            'last_updated',
            'vault_url',
            'service_commands',
            'service_check',
            'service_lb',
            'actions'
        )
        default_columns = (
            'cn',
            'san',
            'status',
            'device',
            'type',
            'install_type'
        )
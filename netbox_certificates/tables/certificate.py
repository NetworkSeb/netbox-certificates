import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from netbox_certificates.models import Certificate

class CertificateTable(NetBoxTable):
    cn = tables.Column(
        linkify=True
    )
    status = ChoiceFieldColumn()
    type = ChoiceFieldColumn()
    term = ChoiceFieldColumn()
    automated = ChoiceFieldColumn()
    service_lb = ChoiceFieldColumn()
    install_type = ChoiceFieldColumn()
    instances = tables.Column()
    ca_id = tables.Column(
        linkify=True
    )
    active = tables.Column(
        linkify=True
    )
    latest = tables.Column(
        linkify=True
    )
    latest__expiry_date = tables.DateTimeColumn(
        verbose_name = "Latest Expiry",
        format='d/m/Y'
    )
    active__expiry_date = tables.DateTimeColumn(
        verbose_name = "Active Expiry",
        format='d/m/Y'
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
            'vm',
            'type',
            'term',
            'install_type', 
            'fs_cert_location', 
            'fs_key_location', 
            'created',
            'last_updated',
            'vault_url',
            'service_commands',
            'service_check',
            'monitor',
            'service_lb',
            'host_consistent',
            'automated',
            'technical_owner',
            'technical_group',
            'business_contact',
            'business_group',
            'infrastructure_contact',
            'infrastructure_group',
            'actions',
            'latest',
            'active',
            'latest__expiry_date',
            'active__expiry_date',
            'latest__infrastructure_installer'
        )
        default_columns = (
            'cn',
            'san',
            'status',
            'device',
            'vm',
            'type',
            'term',
            'install_type',
            'automated',
            'service_lb',
            'host_consistent',
            'latest',
            'active'
        )
import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn, ActionsColumn
from netbox_certificates.models import CertificateAssignment

class CertificateAssignmentTable(NetBoxTable):
    pk = tables.CheckBoxColumn(visible=True)

    ip_address = tables.TemplateColumn(
        template_code='''
            <a href="{{ record.ip_address.get_absolute_url }}">
                {% if record.ip_address.dns_name %}
                    <strong>{{ record.ip_address.dns_name }}</strong>
                    <br><small class="text-muted">{{ record.ip_address.address }}</small>
                {% else %}
                    {{ record.ip_address.address }}
                {% endif %}
            </a>
        ''',
        verbose_name='IP / FQDN'
    )
    service = tables.Column(linkify=True, verbose_name='Service')
    certificate = tables.Column(
        linkify=True,
        verbose_name='Certificate'
    )
    port = tables.Column(verbose_name='Port')
    status = ChoiceFieldColumn(verbose_name='Status')
    # Custom DateTime Format String
    last_verified = tables.DateTimeColumn(
        format='Y-m-d H:i:s',  # Outputs: 2026-09-16 13:34:05
        verbose_name='Last Verified'
    )
    installation_method = ChoiceFieldColumn(verbose_name='Installation Method')

    class Meta(NetBoxTable.Meta):
        model = CertificateAssignment
        fields = (
            'pk', 'id', 'ip_address', 'service', 'certificate', 'port', 
            'status', 'installation_method', 'installed_serial', 'last_verified', 'actions'
        )
        default_columns = ('pk', 'ip_address', 'service', 'certificate', 'port', 'status', 'installation_method', 'last_verified', 'actions')
        order_by = ('ip_address', 'port')

import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn, ActionsColumn
from netbox_certificates.models import CertificateAssignment

class CertificateAssignmentTable(NetBoxTable):
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
    certificate = tables.Column(
        linkify=True,
        verbose_name='Certificate'
    )
    port = tables.Column(verbose_name='Port')
    status = ChoiceFieldColumn(verbose_name='Status')
    last_verified = tables.DateTimeColumn(verbose_name='Last Verified')
    actions = ActionsColumn(actions=('edit', 'delete'))

    class Meta(NetBoxTable.Meta):
        model = CertificateAssignment
        fields = (
            'pk', 'id', 'ip_address', 'certificate', 'port', 
            'status', 'installed_serial', 'last_verified', 'actions'
        )
        default_columns = ('pk', 'ip_address', 'certificate', 'port', 'status', 'last_verified')
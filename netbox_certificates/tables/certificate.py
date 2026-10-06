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
    deployment_count = tables.Column(
        verbose_name='Deployments',
        empty_values=(),
        orderable=True
    )
    deployments = tables.TemplateColumn(
        template_code="""
        {% for assignment in record.assignments.all %}
          <div class="mb-1">
            {% if assignment.ip_address.assigned_object.parent_object %}
                <a href="{{ assignment.ip_address.assigned_object.parent_object.get_absolute_url }}">
                    {{ assignment.ip_address.assigned_object.parent_object }}
                </a>
            {% elif assignment.ip_address.address %}
                {# IP Address link and port #}
                <a href="{{ assignment.ip_address.get_absolute_url }}">
                <span class="">{{ assignment.ip_address.address }}</span>
                </a>
            {% endif %}
          </div>
        {% empty %}
          <span class="text-muted">—</span>
        {% endfor %}
        """,
        verbose_name='Deployed on',
        orderable=False
    )

    class Meta(NetBoxTable.Meta):
        model = Certificate
        fields = (
            'pk',
            'id', 
            'cn', 
            'san',
            'deployments',
            'status',
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
            'instance_count',
            'deployment_count',
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
            'deployments',
            'status',
            'type',
            'term',
            'install_type',
            'instance_count',
            'deployment_count',
            'automated',
            'service_lb',
            'host_consistent',
            'latest',
            'active'
        )
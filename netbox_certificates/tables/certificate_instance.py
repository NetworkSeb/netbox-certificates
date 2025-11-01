import django_tables2 as tables
from django.forms.widgets import NullBooleanSelect
from django.forms import BooleanField

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from netbox_certificates.models import CertificateInstance

class CertificateInstanceTable(NetBoxTable):
    ca_reference = tables.Column(
        linkify=True
    )
    ca = tables.Column(
        linkify=True
    )
    certificate = tables.Column(
        linkify=True
    )
    status = ChoiceFieldColumn()

    issue_date = tables.DateTimeColumn(
        format='Y-m-d'
    )

    expiry_date = tables.DateTimeColumn(
        format='Y-m-d'
    )

    certificate__active__expiry_date = tables.DateTimeColumn(
        verbose_name = "Active Expiry",
        format='Y-m-d'
    )

    certificate__host_consistent = tables.BooleanColumn(
        verbose_name = "Host Consistent?"
    )


    #TODO: Update below so we can see infrastructure_installer in table view.
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
            'status',
            'surpassed',
            'certificate__host_consistent',
            'certificate__active__expiry_date',
            'csr',
            'key',
            'pem',
            'issuer',
            'pubkey_algorithm',
            'pubkey_size',
            'pubkey_sha1',
            'infrastructure_installer',
            'term',
            'tags'
        )
        default_columns = (
            'ca_reference',
            'certificate',
            'serial_number',
            'status',
            'surpassed',
            'certificate__host_consistent',
            'certificate__active__expiry_date',
            'expiry_date',
            'infrastructure_installer',
        )
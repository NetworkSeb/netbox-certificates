from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField

from netbox_certificates.models import CertificateInstance


class CertificateInstanceForm(NetBoxModelForm):

    comments = CommentField()

    class Meta:
        model = CertificateInstance
        fields = (
            'ca_reference',
            'serial_number',
            'issue_date',
            'expiry_date',
            'status'
            'csr',
            'key',
            'pem',
            'comments'
            'tags'    
        )

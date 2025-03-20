from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField
from .certificate import Certificate


class CertificateForm(NetBoxModelForm):

    comments = CommentField()

    class Meta:
        model = Certificate
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

from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField
from . import models


class CertificateInstanceForm(NetBoxModelForm):

    comments = CommentField()

    class Meta:
        model = models.Certificate
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

from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField
from .certificate import Certificate


class CertificateForm(NetBoxModelForm):

    comments = CommentField()

    class Meta:
        model = Certificate
        fields = (
            'name',
            'acme_url',
            'admin_url',
            'status',
            'comments'
            'tags'    
        )
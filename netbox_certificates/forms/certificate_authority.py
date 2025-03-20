from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField
from . import models


class CertificateAuthorityForm(NetBoxModelForm):

    comments = CommentField()

    class Meta:
        model = models.Certificate
        fields = (
            'name',
            'acme_url',
            'admin_url',
            'status',
            'comments'
            'tags'    
        )
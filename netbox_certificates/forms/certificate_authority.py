from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField

from netbox_certificates.models import CertificateAuthority


class CertificateAuthorityForm(NetBoxModelForm):

    comments = CommentField()

    class Meta:
        model = CertificateAuthority
        fields = (
            'name',
            'acme_url',
            'admin_url',
            'status',
            'comments'
            'tags'    
        )
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField

from django import forms

from netbox_certificates.models import CertificateAuthority, CertificateAuthorityStatusChoice, Certificate


class CertificateAuthorityForm(NetBoxModelForm):

    comments = CommentField()

    class Meta:
        model = CertificateAuthority
        verbose_name_plural = "Certificate Authorities"
        fields = (
            'name',
            'acme_url',
            'admin_url',
            'status',
            'comments',
            'tags'    
        )

class CertificateAuthorityFilterForm(NetBoxModelFilterSetForm):
    model = CertificateAuthority

    certificates = forms.ModelMultipleChoiceField(
        queryset=Certificate.objects.all(),
        required=False
    )

    status = forms.MultipleChoiceField(
        choices=CertificateAuthorityStatusChoice,
        required=False
    )
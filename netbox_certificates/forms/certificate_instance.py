from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField

from django import forms

from netbox_certificates.models import CertificateInstance, CertificateInstanceStatusChoices, Certificate, CertificateAuthority


class CertificateInstanceForm(NetBoxModelForm):

    comments = CommentField()

    class Meta:
        model = CertificateInstance
        fields = (
            'ca_reference',
            'certificate',
            'ca',
            'serial_number',
            'issue_date',
            'expiry_date',
            'status',
            'csr',
            'key',
            'pem',
            'comments',
            'tags'    
        )

class CertificateInstanceFilterForm(NetBoxModelFilterSetForm):
    model = CertificateInstance

    certificate_instance = forms.ModelMultipleChoiceField(
        queryset=CertificateInstance.objects.all(),
        required=False
    )

    certificate = forms.ModelMultipleChoiceField(
        queryset=Certificate.objects.all()
    )

    ca = forms.ModelMultipleChoiceField(
        queryset=CertificateAuthority.objects.all(),
        required=False
    )

    issued = forms.DateTimeField(
        required=False
    )

    expiry = forms.DateTimeField(
        required=False
    )

    status = forms.MultipleChoiceField(
        choices=CertificateInstanceStatusChoices,
        required=False
    )

    status = forms.MultipleChoiceField(
        choices=CertificateInstanceStatusChoices,
        required=False
    )

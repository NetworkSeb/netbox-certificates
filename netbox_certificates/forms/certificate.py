from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from dcim.models import Device
from utilities.forms.fields import CommentField, DynamicModelChoiceField, DynamicModelMultipleChoiceField

from netbox_certificates.models import Certificate, CertificateAuthority, CertificateInstance, CertificateInstallChoices, CertificateStatusChoices, CertificateTypeChoices


class CertificateForm(NetBoxModelForm):

    device = DynamicModelMultipleChoiceField(
        queryset=Device.objects.all()
    )

    instances = DynamicModelChoiceField(
        queryset=CertificateInstance.objects.all()
    )

    ca = DynamicModelChoiceField(
        queryset=CertificateAuthority.objects.all()
    )

    comments = CommentField()

    class Meta:
        model = Certificate
        fields = (
            'cn', 
            'san',
            'device',
            'status', 
            'type', 
            'install_type', 
            'fs_cert_location', 
            'fs_key_location', 
            'vault_url',
            'service_commands',
            'service_check',
            'service_lb',
            'ca',
            'content',
            'comments',
            'tags'    
        )

class CertificateFilterForm(NetBoxModelFilterSetForm):
    model = Certificate

    certificates = forms.ModelMultipleChoiceField(
        queryset=Certificate.objects.all(),
        required=False
    )

    device = forms.ModelMultipleChoiceField(
        queryset=Device.objects.all()
    )

    status = forms.MultipleChoiceField(
        choices=CertificateStatusChoices,
        required=False
    )

    type = forms.MultipleChoiceField(
        choices=CertificateTypeChoices,
        required=False
    )

    install_type = forms.MultipleChoiceField(
        choices=CertificateInstallChoices,
        required=False
    )
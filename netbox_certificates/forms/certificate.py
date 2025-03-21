from netbox.forms import NetBoxModelForm
from dcim.models import Device
from utilities.forms.fields import CommentField, DynamicModelChoiceField, DynamicModelMultipleChoiceField

from netbox_certificates.models import Certificate, CertificateAuthority, CertificateInstance


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
            'status', 
            'type', 
            'install_type', 
            'fs_cert_location', 
            'fs_key_location', 
            'vault_url',
            'service_commands',
            'service_check',
            'service_lb',
            'ca_id',
            'comments',
            'tags'    
        )
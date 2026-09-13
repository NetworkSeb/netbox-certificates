from django import forms
from netbox.forms import NetBoxModelForm
from ipam.models import IPAddress
from utilities.forms.fields import DynamicModelChoiceField
from netbox_certificates.models import CertificateAssignment, Certificate

class CertificateAssignmentForm(NetBoxModelForm):
    certificate = DynamicModelChoiceField(
        queryset=Certificate.objects.all(),
        required=True,
        label='Certificate'
    )
    ip_address = DynamicModelChoiceField(
        queryset=IPAddress.objects.all(),
        required=True,
        label='IP Address'
    )

    class Meta:
        model = CertificateAssignment
        fields = (
            'certificate', 'ip_address', 'port', 'status', 
            'installed_serial', 'tags'
        )
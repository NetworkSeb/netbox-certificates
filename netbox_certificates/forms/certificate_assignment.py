from django import forms
from netbox.forms import NetBoxModelForm
from ipam.models import IPAddress, Service
from utilities.forms.fields import DynamicModelChoiceField
from netbox_certificates.models import CertificateAssignment, Certificate

class CertificateAssignmentForm(NetBoxModelForm):
    certificate = DynamicModelChoiceField(
        queryset=Certificate.objects.all(),
        required=True,
        label='Certificate',
        query_params={
            'status': 'issued',
        }
    )
    ip_address = DynamicModelChoiceField(
        queryset=IPAddress.objects.all(),
        required=True,
        label='IP Address'
    )
    # New Field: Dynamic lookup for Application Service
    service = DynamicModelChoiceField(
        queryset=Service.objects.all(),
        required=False,
        label='Application Service',
        # Restrict services dynamically to those bound to the selected IP address
        query_params={
            'ip_address_id': '$ip_address',
        }
    )

    class Meta:
        model = CertificateAssignment
        fields = (
            'certificate', 'ip_address', 'service', 'port', 
            'status', 'installed_serial', 'tags'
        )
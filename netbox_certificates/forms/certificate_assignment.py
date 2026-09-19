from django.forms import MultipleChoiceField
from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm, NetBoxModelBulkEditForm, NetBoxModelImportForm
from ipam.models import IPAddress, Service
from utilities.forms.fields import DynamicModelChoiceField, DynamicModelMultipleChoiceField
from netbox_certificates.models import CertificateAssignment, Certificate, CertificateAssignmentStatusChoices, CertificateInstallationMethodChoices

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
            'status', 'installation_method', 'installed_serial', 'tags'
        )

class CertificateAssignmentFilterForm(NetBoxModelFilterSetForm):
    model = CertificateAssignment

    certificate_id = DynamicModelMultipleChoiceField(
        queryset=Certificate.objects.all(),
        required=False,
        label='Certificate'
    )
    ip_address_id = DynamicModelMultipleChoiceField(
        queryset=IPAddress.objects.all(),
        required=False,
        label='IP Address'
    )
    service_id = DynamicModelMultipleChoiceField(
        queryset=Service.objects.all(),
        required=False,
        label='Service'
    )
    status = MultipleChoiceField(
        choices=CertificateAssignmentStatusChoices,
        required=False
    )
    installation_method = MultipleChoiceField(
        choices=CertificateInstallationMethodChoices,
        required=False,
        label='Installation Method'
    )

class CertificateAssignmentBulkEditForm(NetBoxModelBulkEditForm):
    certificate = DynamicModelChoiceField(
        queryset=Certificate.objects.all(),
        required=False,
        label='Certificate'
    )
    status = forms.ChoiceField(
        choices=CertificateAssignmentStatusChoices,
        required=False,
        widget=forms.Select
    )
    installation_method = forms.ChoiceField(
        choices=CertificateInstallationMethodChoices,
        required=False,
        label='Installation Method',
        widget=forms.Select
    )
    port = forms.IntegerField(
        required=False,
        label='Port'
    )

    model = CertificateAssignment
    fieldsets = (
        (None, ('certificate', 'status', 'installation_method', 'port')),
    )
    nullable_fields = ('port',)

class CertificateAssignmentCSVForm(NetBoxModelImportForm):
    certificate = forms.ModelChoiceField(
        queryset=Certificate.objects.all(),
        to_field_name='cn',
        help_text='Certificate Common Name (CN), e.g. box.net.sussex.ac.uk'
    )
    ip_address = forms.ModelChoiceField(
        queryset=IPAddress.objects.all(),
        to_field_name='address',
        help_text='IP Address (e.g. 192.168.1.10/24)'
    )
    service = forms.ModelChoiceField(
        queryset=Service.objects.all(),
        required=False,
        to_field_name='name',
        help_text='Associated Core Service Name'
    )

    class Meta:
        model = CertificateAssignment
        fields = (
            'certificate',
            'ip_address',
            'service',
            'port',
            'status',
            'installation_method',
            'installed_serial',
        )
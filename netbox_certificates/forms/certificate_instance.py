from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm, NetBoxModelImportForm, NetBoxModelBulkEditForm
from tenancy.models import Contact
from utilities.forms.fields import CommentField
from utilities.forms.widgets import DateTimePicker
from utilities.forms import BOOLEAN_WITH_BLANK_CHOICES

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
            'surpassed',
            'csr',
            'key',
            'pem',
            'issuer',
            'pubkey_algorithm',
            'pubkey_size',
            'pubkey_sha1',
            'term',
            'infrastructure_installer',
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
        queryset=Certificate.objects.all(),
        required=False
    )

    ca = forms.ModelMultipleChoiceField(
        queryset=CertificateAuthority.objects.all(),
        required=False
    )

    issued = forms.DateTimeField(
        required=False,
        widget=DateTimePicker()
    )

    expiry = forms.DateTimeField(
        required=False,
        widget=DateTimePicker()
    )

    status = forms.MultipleChoiceField(
        choices=CertificateInstanceStatusChoices,
        required=False
    )

    surpassed = forms.BooleanField(
        required=False,
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES)
    )

    infrastructure_installer = forms.ModelMultipleChoiceField(
        queryset=Contact.objects.all(),
        required=False
    )

class CertificateInstanceImportFrom(NetBoxModelImportForm):
    ca_reference = forms.CharField(
        label=("Certificate Authority Reference (order number)")
    )

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
            'surpassed',
            'csr',
            'key',
            'pem',
            'issuer',
            'pubkey_algorithm',
            'pubkey_size',
            'pubkey_sha1',
            'term',
            'infrastructure_installer',
            'comments',
            'tags'    
        )

class CertificateInstanceBulkEditForm(NetBoxModelBulkEditForm):
    model = CertificateInstance
    
    certificate_instance = forms.ModelMultipleChoiceField(
        queryset=CertificateInstance.objects.all(),
        required=False
    )

    certificate = forms.ModelMultipleChoiceField(
        queryset=Certificate.objects.all(),
        required=False
    )

    ca = forms.ModelMultipleChoiceField(
        queryset=CertificateAuthority.objects.all(),
        required=False
    )

    issued = forms.DateTimeField(
        required=False,
        widget=DateTimePicker()
    )

    expiry = forms.DateTimeField(
        required=False,
        widget=DateTimePicker()
    )

    status = forms.ChoiceField(
        choices=CertificateInstanceStatusChoices,
        required=False
    )

    surpassed = forms.BooleanField(
        required=False,
    )

    infrastructure_installer = forms.ModelMultipleChoiceField(
        queryset=Contact.objects.all(),
        required=False
    )
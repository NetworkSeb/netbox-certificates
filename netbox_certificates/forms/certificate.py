from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm, NetBoxModelImportForm
from dcim.models import Device
from virtualization.models import VirtualMachine
from tenancy.models import Contact, ContactGroup
from utilities.forms.fields import CommentField, DynamicModelChoiceField, DynamicModelMultipleChoiceField
from django import forms

from netbox_certificates.models import Certificate, CertificateAuthority, CertificateInstance, CertificateInstallChoices, CertificateStatusChoices, CertificateTypeChoices


class CertificateForm(NetBoxModelForm):

    device = DynamicModelMultipleChoiceField(
        queryset=Device.objects.all(),
        required=False
    )

    vm = DynamicModelMultipleChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False
    )

    instances = DynamicModelChoiceField(
        queryset=CertificateInstance.objects.all(),
        required=False
    )

    comments = CommentField()

    class Meta:
        model = Certificate
        fields = (
            'cn', 
            'san',
            'device',
            'vm',
            'status', 
            'type', 
            'install_type', 
            'fs_cert_location', 
            'fs_key_location', 
            'vault_url',
            'service_commands',
            'service_check',
            'service_lb',
            'automated',
            'technical_owner',
            'technical_group',
            'business_contact',
            'business_group',
            'infrastructure_contact',
            'infrastructure_group',
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
        queryset=Device.objects.all(),
        required=False
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

    technical_owner = forms.ModelMultipleChoiceField(
        queryset=Contact.objects.all(),
        required=False
    )

    business_contact = forms.ModelMultipleChoiceField(
        queryset=Contact.objects.all(),
        required=False
    )

    infrastructure_contact = forms.ModelMultipleChoiceField(
        queryset=Contact.objects.all(),
        required=False
    )

    technical_group = forms.ModelMultipleChoiceField(
        queryset=ContactGroup.objects.all(),
        required=False
    )

    business_group = forms.ModelMultipleChoiceField(
        queryset=ContactGroup.objects.all(),
        required=False
    )

    infrastructure_group = forms.ModelMultipleChoiceField(
        queryset=ContactGroup.objects.all(),
        required=False
    )

class CertificateImportFrom(NetBoxModelImportForm):
    cn = forms.CharField(
        label=("Common Name")
    )

    class Meta:
        model = Certificate
        fields = (
            'cn', 
            'san',
            'device',
            'vm',
            'status', 
            'type',
            'term',
            'install_type', 
            'fs_cert_location', 
            'fs_key_location', 
            'vault_url',
            'service_commands',
            'service_check',
            'service_lb',
            'automated',
            'technical_owner',
            'technical_group',
            'business_contact',
            'business_group',
            'infrastructure_contact',
            'infrastructure_group',
            'content',
            'comments',
            'tags'    
        )
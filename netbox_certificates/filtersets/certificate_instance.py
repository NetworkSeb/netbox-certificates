from netbox.filtersets import NetBoxModelFilterSet
from django.db import models
import django_filters
from django import forms
from taggit.managers import TaggableManager
from utilities.filtersets import register_filterset

from netbox_certificates.models import CertificateInstance

@register_filterset
class CertificateInstanceFilterSet(NetBoxModelFilterSet):

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
        filter_overrides= {
            TaggableManager: {
                'filter_class': django_filters.CharFilter
            }
        }

    def search(self, queryset, name, value):
        return queryset.filter(certificate__cn__icontains=value)
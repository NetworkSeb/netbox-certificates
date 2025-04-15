from netbox.filtersets import NetBoxModelFilterSet
from django.db import models
import django_filters
from django_filters import CharFilter
from django import forms
from django.contrib.postgres.fields import ArrayField
from taggit.managers import TaggableManager

from netbox_certificates.models import CertificateInstance

class CertificateInstanceFilterSet(NetBoxModelFilterSet):

    certificate = CharFilter(lookup_expr="icontains", label="Certificate")

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
            ArrayField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
            models.BooleanField: {
                 'filter_class': django_filters.BooleanFilter,
                 'extra': lambda f: {
                     'widget': forms.CheckboxInput,
                 },
             },
            TaggableManager: {
                'filter_class': django_filters.CharFilter
            }
        }

    def search(self, queryset, name, value):
        return queryset.filter(ca_reference__icontains=value)
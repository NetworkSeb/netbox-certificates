from netbox.filtersets import NetBoxModelFilterSet
from django.db import models
import django_filters
from django import forms
from django.contrib.postgres.fields import ArrayField

from netbox_certificates.models import Certificate

class CertificateFilterSet(NetBoxModelFilterSet):

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
        }

    def search(self, queryset, name, value):
        return queryset.filter(cn__icontains=value)
    
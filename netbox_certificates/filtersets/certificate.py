from netbox.filtersets import NetBoxModelFilterSet
from django.db import models
import django_filters
from django import forms
from django.contrib.postgres.fields import ArrayField
from taggit.managers import TaggableManager

from netbox_certificates.models import Certificate

class CertificateFilterSet(NetBoxModelFilterSet):

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
        return queryset.filter(cn__icontains=value)
    
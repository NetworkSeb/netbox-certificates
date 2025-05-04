from netbox.filtersets import NetBoxModelFilterSet
from django.db import models
import django_filters
from django import forms
from taggit.managers import TaggableManager

from netbox_certificates.models import CertificateAuthority

class CertificateAuthorityFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = CertificateAuthority
        fields = (
            'name',
            'org_id',
            'cert_profile_ev_id',
            'cert_profile_ov_id',
            'acme_url',
            'admin_url',
            'status',
            'comments',
            'tags'
        )
        filter_overrides= {
            TaggableManager: {
                'filter_class': django_filters.CharFilter
            }
        }

    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)
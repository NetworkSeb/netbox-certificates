import strawberry_django

from netbox.graphql.filter_mixins import autotype_decorator, BaseFilterMixin

from netbox_certificates.models import (
    Certificate,
    CertificateInstance,
    CertificateAuthority
)

from netbox_certificates.filtersets import (
    CertificateFilterSet,
    CertificateInstanceFilterSet,
    CertificateAuthorityFilterSet
)

@strawberry_django.filter_type(Certificate, lookups=True)
#@autotype_decorator(CertificateFilterSet)
class NetBoxCertificateFilter(BaseFilterMixin):
    pass

@strawberry_django.filter_type(CertificateInstance, lookups=True)
#@autotype_decorator(CertificateInstanceFilterSet)
class NetBoxCertificateInstanceFilter(BaseFilterMixin):
    pass

@strawberry_django.filter_type(CertificateAuthority, lookups=True)
#@autotype_decorator(CertificateAuthorityFilterSet)
class NetBoxCertificateAuthorityFilter(BaseFilterMixin):
    pass
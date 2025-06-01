import strawberry_django

from netbox.graphql.filter_mixins import NetBoxModelFilterMixin

from netbox_certificates.models import (
    Certificate,
    CertificateInstance,
    CertificateAuthority
)

@strawberry_django.filter_type(Certificate, lookups=True)
class NetBoxCertificateFilter(NetBoxModelFilterMixin):
    pass

@strawberry_django.filter_type(CertificateInstance, lookups=True)
class NetBoxCertificateInstanceFilter(NetBoxModelFilterMixin):
    pass

@strawberry_django.filter_type(CertificateAuthority, lookups=True)
class NetBoxCertificateAuthorityFilter(NetBoxModelFilterMixin):
    pass
import strawberry_django

from netbox.graphql.filters import NetBoxModelFilter

from netbox_certificates.models import (
    Certificate,
    CertificateInstance,
    CertificateAuthority
)

@strawberry_django.filter_type(Certificate, lookups=True)
class NetBoxCertificateFilter(NetBoxModelFilter):
    pass

@strawberry_django.filter_type(CertificateInstance, lookups=True)
class NetBoxCertificateInstanceFilter(NetBoxModelFilter):
    pass

@strawberry_django.filter_type(CertificateAuthority, lookups=True)
class NetBoxCertificateAuthorityFilter(NetBoxModelFilter):
    pass
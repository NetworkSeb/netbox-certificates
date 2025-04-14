from netbox.search import SearchIndex, register_search

from netbox_certificates.models import Certificate, CertificateInstance, CertificateAuthority

@register_search
class CertificateIndex(SearchIndex):
    model = Certificate
    fields = (
        ('cn', 100),
        ('san', 150),
        ('comments', 5000),
    )

@register_search
class CertificateInstanceIndex(SearchIndex):
    model = CertificateInstance
    fields = (
        ('ca_reference', 200),
        ('serial_number', 250),
        ('comments', 5000),
    )

@register_search
class CertificateAuthorityIndex(SearchIndex):
    model = CertificateAuthority
    fields = (
        ('name', 300),
        ('comments', 5000),
    )
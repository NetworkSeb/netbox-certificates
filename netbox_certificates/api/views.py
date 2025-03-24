from netbox.api.viewsets import NetBoxModelViewSet
from django.db.models import Count

from netbox_certificates.filtersets import CertificateFilterSet, CertificateInstanceFilterSet, CertificateAuthorityFilterSet
from netbox_certificates.models import Certificate, CertificateAuthority, CertificateInstance
from netbox_certificates.api.serializers_ import CertificateSerializer, CertificateAuthoritySerializer, CertificateInstanceSerializer


class CertificateViewSet(NetBoxModelViewSet):
    queryset = Certificate.objects.prefetch_related('id','cn', 'san','tags').annotate(
        instance_count=Count('instances')
    )
    serializer_class = CertificateSerializer
    filterset_class = CertificateFilterSet

class CertificateInstanceViewSet(NetBoxModelViewSet):
    queryset = CertificateInstance.objects.prefetch_related('id','certificate','ca','tags')
    serializer_class = CertificateInstanceSerializer
    filterset_class=CertificateInstanceFilterSet

class CertificateAuthorityViewSet(NetBoxModelViewSet):
    queryset = CertificateAuthority.objects.prefetch_related('id','name','tags').annotate(
        certificate_count=Count('certificates')
    )
    serializer_class = CertificateAuthoritySerializer
    filterset_class = CertificateAuthorityFilterSet

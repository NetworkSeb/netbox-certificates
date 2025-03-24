from netbox.api.viewsets import NetBoxModelViewSet
from django.db.models import Count

from netbox_certificates.filtersets import *
from netbox_certificates.models import *
from netbox_certificates.api.serializers_ import CertificateSerializer, CertificateInstanceSerializer, CertificateAuthoritySerializer

class CertificateViewSet(NetBoxModelViewSet):
    queryset = Certificate.objects.prefetch_releated('id','cn', 'san','tags').annotate(
        instance_count=Count('instances')
    )
    serializer_class = CertificateSerializer
    filerset_class = CertificateFilterSet

class CertificateInstanceViewSet(NetBoxModelViewSet):
    queryset = Certificate.objects.prefetch_releated('id','certificate','ca','tags')
    serializer_class = CertificateInstanceSerializer
    filterset_class=CertificateInstanceFilterSet

class CertificateAuthorityViewSet(NetBoxModelViewSet):
    queryset = Certificate.objects.prefetch_releated('id','name','tags').annotate(
        certificate_count=Count('certificates')
    )
    serializer_class = CertificateAuthoritySerializer
    filterset_class = CertificateAuthorityFilterSet

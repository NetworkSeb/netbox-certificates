from netbox.api.viewsets import NetBoxModelViewSet
from django.db.models import Count

from netbox_certificates.filtersets import CertificateFilterSet, CertificateInstanceFilterSet, CertificateAuthorityFilterSet, CertificateAssignmentFilterSet
from netbox_certificates.models import Certificate, CertificateAuthority, CertificateInstance, CertificateAssignment
from netbox_certificates.api.serializers_ import CertificateSerializer, CertificateAuthoritySerializer, CertificateInstanceSerializer, CertificateAssignmentSerializer


class CertificateViewSet(NetBoxModelViewSet):
    queryset = Certificate.objects.all().annotate(
        instance_count=Count('instances')
    )
    serializer_class = CertificateSerializer
    filterset_class = CertificateFilterSet

class CertificateInstanceViewSet(NetBoxModelViewSet):
    queryset = CertificateInstance.objects.all()
    serializer_class = CertificateInstanceSerializer
    filterset_class=CertificateInstanceFilterSet

class CertificateAuthorityViewSet(NetBoxModelViewSet):
    queryset = CertificateAuthority.objects.all().annotate(
        certificate_count=Count('certificates')
    )
    serializer_class = CertificateAuthoritySerializer
    filterset_class = CertificateAuthorityFilterSet

class CertificateAssignmentViewSet(NetBoxModelViewSet):
    queryset = CertificateAssignment.objects.all()
    serializer_class = CertificateAssignmentSerializer
    filterset_class = CertificateAssignmentFilterSet

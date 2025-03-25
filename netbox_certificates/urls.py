from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from netbox_certificates.views import CertificateListView, CertificateEditView, CertificateView, CertificateDeleteView, CertificateInstanceListView, CertificateInstanceEditView, CertificateInstanceView, CertificateInstanceDeleteView, CertificateAuthorityListView, CertificateAuthorityEditView, CertificateAuthorityView, CertificateAuthorityDeleteView
from netbox_certificates.models import Certificate, CertificateInstance, CertificateAuthority

urlpatterns = (

    # Certificates
    path('certificates/', CertificateListView.as_view(), name='certificate_list'),
    path('certificates/add/', CertificateEditView.as_view(), name='certificate_add'),
    path('certificates/<int:pk>/', CertificateView.as_view(), name='certificate'),
    path('certificates/<int:pk>/edit/', CertificateEditView.as_view(), name='certificate_edit'),
    path('certificates/<int:pk>/delete/', CertificateDeleteView.as_view(), name='certificate_delete'),
    path('certificates/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='certificate_changelog', kwargs={'model': Certificate}),

    # Certificate Instances
    path('certificate-instance/', CertificateInstanceListView.as_view(), name='certificate_instance_list'),
    path('certificate-instance/add/', CertificateInstanceEditView.as_view(), name='certificate_instance_add'),
    path('certificate-instance/<int:pk>/', CertificateInstanceView.as_view(), name='certificate_instance'),
    path('certificate-instance/<int:pk>/edit/', CertificateInstanceEditView.as_view(), name='certificateinstance_edit'),
    path('certificate-instance/<int:pk>/delete/', CertificateInstanceDeleteView.as_view(), name='certificateinstance_delete'),
    path('certificate-instance/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='certificateinstance_changelog', kwargs={'model': CertificateInstance}),

    # Certificate Authorities
    path('certificate-authority/', CertificateAuthorityListView.as_view(), name='certificate_authority_list'),
    path('certificate-authority/add/', CertificateAuthorityEditView.as_view(), name='certificate_authority_add'),
    path('certificate-authority/<int:pk>/', CertificateAuthorityView.as_view(), name='certificate_authority'),
    path('certificate-authority/<int:pk>/edit/', CertificateAuthorityEditView.as_view(), name='certificateauthority_edit'),
    path('certificate-authority/<int:pk>/delete/', CertificateAuthorityDeleteView.as_view(), name='certificateauthority_delete'),
    path('certificate-authority/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='certificateauthority_changelog', kwargs={'model': CertificateAuthority}),
)
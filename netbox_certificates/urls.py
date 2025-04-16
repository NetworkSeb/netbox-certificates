from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from utilities.urls import get_model_urls

from netbox_certificates.views import *
from netbox_certificates.models import Certificate, CertificateInstance, CertificateAuthority

urlpatterns = (

    # Certificates
    path('certificates/', CertificateListView.as_view(), name='certificate_list'),
    path('certificates/add/', CertificateEditView.as_view(), name='certificate_add'),
    path('certificates/<int:pk>/', CertificateView.as_view(), name='certificate'),
    path('certificates/<int:pk>/edit/', CertificateEditView.as_view(), name='certificate_edit'),
    path('certificates/<int:pk>/delete/', CertificateDeleteView.as_view(), name='certificate_delete'),
    path('certificates/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='certificate_changelog', kwargs={'model': Certificate}),
    path("certificates/bulk_import/", CertificateBulkImportView.as_view(), name='certificate_bulkimport'),

    # Certificate Instances
    path('certificateinstance/', CertificateInstanceListView.as_view(), name='certificateinstance_list'),
    path('certificateinstance/add/', CertificateInstanceEditView.as_view(), name='certificateinstance_add'),
    path('certificateinstance/<int:pk>/', CertificateInstanceView.as_view(), name='certificateinstance'),
    path('certificateinstance/<int:pk>/edit/', CertificateInstanceEditView.as_view(), name='certificateinstance_edit'),
    path('certificateinstance/<int:pk>/delete/', CertificateInstanceDeleteView.as_view(), name='certificateinstance_delete'),
    path('certificateinstance/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='certificateinstance_changelog', kwargs={'model': CertificateInstance}),
    path("certificatesinstance/bulk_import/", CertificateInstanceBulkImportView.as_view(), name='certificateinstance_bulkimport'),

    # Certificate Authorities
    path('certificateauthority/', CertificateAuthorityListView.as_view(), name='certificateauthority_list'),
    path('certificateauthority/add/', CertificateAuthorityEditView.as_view(), name='certificateauthority_add'),
    path('certificateauthority/<int:pk>/', CertificateAuthorityView.as_view(), name='certificateauthority'),
    path('certificateauthority/<int:pk>/edit/', CertificateAuthorityEditView.as_view(), name='certificateauthority_edit'),
    path('certificateauthority/<int:pk>/delete/', CertificateAuthorityDeleteView.as_view(), name='certificateauthority_delete'),
    path('certificateauthority/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='certificateauthority_changelog', kwargs={'model': CertificateAuthority}),
)
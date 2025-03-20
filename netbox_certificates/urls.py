from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views

urlpatterns = (

    # Certificates
    path('certificates/', views.CertificateListView.as_view(), name='certificate_list'),
    path('certificates/add/', views.CertificateEditView.as_view(), name='certificate_add'),
    path('certificates/<int:pk>/', views.CertificateView.as_view(), name='certificate'),
    path('certificates/<int:pk>/edit/', views.CertificateEditView.as_view(), name='certificate_edit'),
    path('certificates/<int:pk>/delete/', views.CertificateDeleteView.as_view(), name='certificate_delete'),
    path('certificates/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='certificate_changelog', kwargs={'model': models.Certificate}),

    # Certificate Instances
    path('certificate-instance/', views.CertificateInstanceListView.as_view(), name='certificate_instance_list'),
    path('certificate-instance/add/', views.CertificateInstanceEditView.as_view(), name='certificate_instance_add'),
    path('certificate-instance/<int:pk>/', views.CertificateInstanceView.as_view(), name='certificate_instance'),
    path('certificate-instance/<int:pk>/edit/', views.CertificateInstanceEditView.as_view(), name='certificate_instance_edit'),
    path('certificate-instance/<int:pk>/delete/', views.CertificateInstanceDeleteView.as_view(), name='certificate_instance_delete'),
    path('certificate-instance/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='certificate_instance_changelog', kwargs={'model': models.CertificateInstance}),

    # Certificate Authorities
    path('certificate-authority/', views.CertificateAuthorityListView.as_view(), name='certificate_authority_list'),
    path('certificate-authority/add/', views.CertificateAuthorityEditView.as_view(), name='certificate_authority_add'),
    path('certificate-authority/<int:pk>/', views.CertificateVAuthorityiew.as_view(), name='certificate_authority'),
    path('certificate-authority/<int:pk>/edit/', views.CertificateAuthorityEditView.as_view(), name='certificate_authority_edit'),
    path('certificate-authority/<int:pk>/delete/', views.CertificateAuthorityDeleteView.as_view(), name='certificate_authority_delete'),
    path('certificate-authority/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='certificate_authority_changelog', kwargs={'model': models.CertificateAuthority}),
)
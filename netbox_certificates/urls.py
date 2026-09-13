from django.urls import path, include
from netbox.views.generic import ObjectChangeLogView
from utilities.urls import get_model_urls

from netbox_certificates.views import *
from netbox_certificates.models import Certificate, CertificateInstance, CertificateAuthority

urlpatterns = (

    # Certificates
    path(
        'certificates/', include(get_model_urls("netbox_certificates", "certificate", detail=False))
    ),
    path(
        'certificates/<int:pk>/', include(get_model_urls("netbox_certificates", "certificate"))
    ),

    # Certificate Instances
    path(
        'certificateinstance/', include(get_model_urls("netbox_certificates", "certificateinstance", detail=False))
    ),
    path(
        'certificateinstance/<int:pk>/', include(get_model_urls("netbox_certificates", "certificateinstance"))
    ),

    # Certificate Authorities
    path(
        'certificateauthority/', include(get_model_urls("netbox_certificates", "certificateauthority", detail=False))
    ),
    path(
        'certificateauthority/<int:pk>/', include(get_model_urls("netbox_certificates", "certificateauthority"))
    ),

    # CertificateAssignment UI Routes
    path('assignments/', CertificateAssignmentListView.as_view(), name='certificateassignment_list'),
    path('assignments/add/', CertificateAssignmentEditView.as_view(), name='certificateassignment_add'),
    path('assignments/<int:pk>/', CertificateAssignmentView.as_view(), name='certificateassignment'),
    path('assignments/<int:pk>/edit/', CertificateAssignmentEditView.as_view(), name='certificateassignment_edit'),
    path('assignments/<int:pk>/delete/', CertificateAssignmentDeleteView.as_view(), name='certificateassignment_delete'),
    path('assignments/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='certificateassignment_changelog', kwargs={'model': CertificateAssignment}),

)
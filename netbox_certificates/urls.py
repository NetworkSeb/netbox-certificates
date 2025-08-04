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
)
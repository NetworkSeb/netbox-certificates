from netbox.api.routers import NetBoxRouter

from netbox_certificates.api.views import CertificateViewSet, CertificateInstanceViewSet, CertificateAuthorityViewSet 

app_name = 'netbox_certificates'

router = NetBoxRouter()
router.register('certificates', CertificateViewSet)
router.register('certificate-instance', CertificateInstanceViewSet)
router.register('certificate-authority', CertificateAuthorityViewSet)

urlpatterns=router.urls
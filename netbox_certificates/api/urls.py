from netbox.api.routers import NetBoxRouter

from netbox_certificates.api.views import *

app_name = 'netbox_certificates'

router = NetBoxRouter()
router.register('certificates', CertificateViewSet)
router.register('certificateinstance', CertificateInstanceViewSet)
router.register('certificateauthority', CertificateAuthority)

urlpatterns = router.urls
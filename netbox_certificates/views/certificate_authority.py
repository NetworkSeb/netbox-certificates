from netbox.views import generic
from django.db.models import Count

from netbox_certificates.models import CertificateAuthority
from netbox_certificates.forms import CertificateAuthorityForm
from netbox_certificates.tables import CertificateAuthorityTable

class CertificateAuthorityView(generic.ObjectView):
    queryset = CertificateAuthority.objects.all()

class CertificateAuthorityListView(generic.ObjectListView):
    queryset = CertificateAuthority.objects.annotate(
        certificate_count = Count('certificates')
    )
    table = CertificateAuthorityTable

class CertificateAuthorityEditView(generic.ObjectEditView):
    queryset = CertificateAuthority.objects.all()
    form = CertificateAuthorityForm

class CertificateAuthorityDeleteView(generic.ObjectDeleteView):
    queryset = CertificateAuthority.objects.all()
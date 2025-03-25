from netbox.views import generic
from django.db.models import Count

from netbox_certificates.models import CertificateAuthority
from netbox_certificates.forms import CertificateAuthorityForm, CertificateAuthorityFilterForm
from netbox_certificates.tables import CertificateAuthorityTable, CertificateTable
from netbox_certificates.filtersets import CertificateAuthorityFilterSet

class CertificateAuthorityView(generic.ObjectView):
    queryset = CertificateAuthority.objects.all()

    def get_extra_context(self, request, instance):
        table = CertificateTable(instance.certificates.all())
        table.configure(request)

        return {
            'certificate_table': table
        }

class CertificateAuthorityListView(generic.ObjectListView):
    queryset = CertificateAuthority.objects.annotate(
        certificate_count = Count('certificates')
    )
    table = CertificateAuthorityTable
    filterset=CertificateAuthorityFilterSet
    filterset_form = CertificateAuthorityFilterForm
    

class CertificateAuthorityEditView(generic.ObjectEditView):
    queryset = CertificateAuthority.objects.all()
    form = CertificateAuthorityForm

class CertificateAuthorityDeleteView(generic.ObjectDeleteView):
    queryset = CertificateAuthority.objects.all()
from netbox.views import generic
from django.db.models import Count
from utilities.views import register_model_view

from netbox_certificates.models import Certificate
from netbox_certificates.forms import CertificateForm, CertificateFilterForm, CertificateImportFrom
from netbox_certificates.tables import CertificateTable, CertificateInstanceTable
from netbox_certificates.filtersets import CertificateFilterSet

class CertificateView(generic.ObjectView):
    queryset = Certificate.objects.all()

    def get_extra_context(self, request, instance):
        table = CertificateInstanceTable(instance.instances.all())
        table.configure(request)

        return {
            'instances_table': table
        }

class CertificateListView(generic.ObjectListView):
    queryset = Certificate.objects.annotate(
        instance_count = Count('instances')
    )
    table = CertificateTable
    filterset=CertificateFilterSet
    filterset_form = CertificateFilterForm

class CertificateEditView(generic.ObjectEditView):
    queryset = Certificate.objects.all()
    form = CertificateForm

class CertificateDeleteView(generic.ObjectDeleteView):
    queryset = Certificate.objects.all()

#@register_model_view(Certificate, "bulk_import", detail=False)
class CertificateBulkImportView(generic.BulkImportView):
    queryset = Certificate.objects.all()
    model_form = CertificateImportFrom
    table = CertificateTable
    default_return_url = "plugins:netbox_certificates:certificate_list"
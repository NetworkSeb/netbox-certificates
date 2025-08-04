from netbox.views import generic
from django.db.models import Count
from utilities.views import register_model_view

from netbox_certificates.models import Certificate
from netbox_certificates.forms import CertificateForm, CertificateFilterForm, CertificateImportFrom, CertificateBulkEditForm
from netbox_certificates.tables import CertificateTable, CertificateInstanceTable
from netbox_certificates.filtersets import CertificateFilterSet

__all__ = (
    "CertificateView",
    "CertificateListView",
    "CertificateEditView",
    "CertificateDeleteView",
    "CertificateBulkImportView",
    "CertificateBulkDeleteView",
)

@register_model_view(Certificate)
class CertificateView(generic.ObjectView):
    queryset = Certificate.objects.all()

    def get_extra_context(self, request, instance):
        table = CertificateInstanceTable(instance.instances.all())
        table.configure(request)

        return {
            'instances_table': table
        }

@register_model_view(Certificate, "list", path="", detail=False)
class CertificateListView(generic.ObjectListView):
    queryset = Certificate.objects.annotate(
        instance_count = Count('instances')
    )
    table = CertificateTable
    filterset=CertificateFilterSet
    filterset_form = CertificateFilterForm

@register_model_view(Certificate, "add", detail=False)
@register_model_view(Certificate, "edit")
class CertificateEditView(generic.ObjectEditView):
    queryset = Certificate.objects.all()
    form = CertificateForm

@register_model_view(Certificate, "delete")
class CertificateDeleteView(generic.ObjectDeleteView):
    queryset = Certificate.objects.all()
    model = Certificate
    success_url = "plugins:netbox_certificates:certificate_list"
    default_return_url = "plugins:netbox_certificates:certificate_list"

@register_model_view(Certificate, "bulk_import", detail=False)
class CertificateBulkImportView(generic.BulkImportView):
    queryset = Certificate.objects.all()
    model_form = CertificateImportFrom
    table = CertificateTable
    default_return_url = "plugins:netbox_certificates:certificate_list"

@register_model_view(Certificate, "bulk_edit", path="edit", detail=False)
class CertificateBulkEditView(generic.BulkEditView):
    queryset = Certificate.objects.all()
    filterset = CertificateFilterSet
    table = CertificateTable
    form = CertificateBulkEditForm

@register_model_view(Certificate, "bulk_delete", path="delete", detail=False)
class CertificateBulkDeleteView(generic.BulkDeleteView):
    queryset = Certificate.objects.all()
    filterset = CertificateFilterSet
    table = CertificateTable
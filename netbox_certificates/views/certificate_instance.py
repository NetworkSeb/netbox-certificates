from netbox.views import generic
from django.db.models import Count
from utilities.views import register_model_view

from netbox_certificates.models import CertificateInstance
from netbox_certificates.forms import CertificateInstanceForm, CertificateInstanceFilterForm, CertificateInstanceImportFrom
from netbox_certificates.tables import CertificateInstanceTable
from netbox_certificates.filtersets import CertificateInstanceFilterSet

__all__ = (
    "CertificateInstanceView",
    "CertificateInstanceListView",
    "CertificateInstanceEditView",
    "CertificateInstanceDeleteView",
    "CertificateInstanceBulkImportView",
    "CertificateInstanceBulkDeleteView",
)

@register_model_view(CertificateInstance)
class CertificateInstanceView(generic.ObjectView):
    queryset = CertificateInstance.objects.all()

@register_model_view(CertificateInstance, "list", path="", detail=False)
class CertificateInstanceListView(generic.ObjectListView):
    queryset = CertificateInstance.objects.all()
    table = CertificateInstanceTable
    filterset=CertificateInstanceFilterSet
    filterset_form = CertificateInstanceFilterForm

@register_model_view(CertificateInstance, "add", detail=False)
@register_model_view(CertificateInstance, "edit")
class CertificateInstanceEditView(generic.ObjectEditView):
    queryset = CertificateInstance.objects.all()
    form = CertificateInstanceForm

@register_model_view(CertificateInstance, "delete")
class CertificateInstanceDeleteView(generic.ObjectDeleteView):
    queryset = CertificateInstance.objects.all()

@register_model_view(CertificateInstance, "bulk_import", detail=False)
class CertificateInstanceBulkImportView(generic.BulkImportView):
    queryset = CertificateInstance.objects.all()
    model_form = CertificateInstanceImportFrom
    table = CertificateInstanceTable
    default_return_url = "plugins:netbox_certificates:certificateinstance_list"

@register_model_view(CertificateInstance, "bulk_delete", path="delete", detail=False)
class CertificateInstanceBulkDeleteView(generic.BulkDeleteView):
    queryset = CertificateInstance.objects.all()
    filterset = CertificateInstanceFilterSet
    table = CertificateInstanceTable
from netbox.views import generic
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.db.models import Count
from utilities.views import register_model_view

from netbox_certificates.models import CertificateInstance
from netbox_certificates.forms import CertificateInstanceForm, CertificateInstanceFilterForm, CertificateInstanceImportFrom, CertificateInstanceBulkEditForm
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


@register_model_view(CertificateInstance, "bulk_edit", path="edit", detail=False)
class CertificateInstanceBulkEditView(generic.BulkEditView):
    queryset = CertificateInstance.objects.all()
    filterset = CertificateInstanceFilterSet
    table = CertificateInstanceTable
    form = CertificateInstanceBulkEditForm

@register_model_view(CertificateInstance, "bulk_delete", path="delete", detail=False)
class CertificateInstanceBulkDeleteView(generic.BulkDeleteView):
    queryset = CertificateInstance.objects.all()
    filterset = CertificateInstanceFilterSet
    table = CertificateInstanceTable

@register_model_view(CertificateInstance, name="calendar", detail=False)
class CertificateInstanceCalendarView(TemplateView):
    template_name = "netbox_certificates/certificates.ics"
    """
    Render all certificate instances as an iCal feed
    """
    def get(self, request):
        context = self.get_context_data()
        template_name = "netbox_certificates/certificates.ics"
        certificates = CertificateInstance.objects.order_by('expiry_date').all()
        return render(request, template_name, locals(), content_type='text/calendar')

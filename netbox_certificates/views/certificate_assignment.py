from netbox.views import generic
from utilities.views import register_model_view

from netbox_certificates.models import CertificateAssignment
from netbox_certificates.forms import CertificateAssignmentForm, CertificateAssignmentFilterForm, CertificateAssignmentBulkEditForm, CertificateAssignmentCSVForm
from netbox_certificates.tables import CertificateAssignmentTable
from netbox_certificates.filtersets import CertificateAssignmentFilterSet

__all__ = (
    "CertificateAssignmentView",
    "CertificateAssignmentListView",
    "CertificateAssignmentEditView",
    "CertificateAssignmentDeleteView"
)

@register_model_view(CertificateAssignment)
class CertificateAssignmentView(generic.ObjectView):
    queryset = CertificateAssignment.objects.all()

@register_model_view(CertificateAssignment, 'list', path="", detail=False)
class CertificateAssignmentListView(generic.ObjectListView):
    queryset = CertificateAssignment.objects.all()
    table = CertificateAssignmentTable
    filterset = CertificateAssignmentFilterSet
    filterset_form = CertificateAssignmentFilterForm

@register_model_view(CertificateAssignment, 'add', path='add', detail=False)
@register_model_view(CertificateAssignment, 'edit', path='edit')
class CertificateAssignmentEditView(generic.ObjectEditView):
    queryset = CertificateAssignment.objects.all()
    form = CertificateAssignmentForm

@register_model_view(CertificateAssignment, 'delete', path='delete')
class CertificateAssignmentDeleteView(generic.ObjectDeleteView):
    queryset = CertificateAssignment.objects.all()

@register_model_view(CertificateAssignment, 'bulk_edit', path='edit', detail=False)
class CertificateAssignmentBulkEditView(generic.BulkEditView):
    queryset = CertificateAssignment.objects.all()
    filterset = CertificateAssignmentFilterSet
    table = CertificateAssignmentTable
    form = CertificateAssignmentBulkEditForm

@register_model_view(CertificateAssignment, 'bulk_delete', path='delete', detail=False)
class CertificateAssignmentBulkDeleteView(generic.BulkDeleteView):
    queryset = CertificateAssignment.objects.all()
    table = CertificateAssignmentTable
    filterset = CertificateAssignmentFilterSet

@register_model_view(CertificateAssignment, 'bulk_import', path='import', detail=False)
class CertificateAssignmentBulkImportView(generic.BulkImportView):
    queryset = CertificateAssignment.objects.all()
    model_form = CertificateAssignmentCSVForm
    table = CertificateAssignmentTable

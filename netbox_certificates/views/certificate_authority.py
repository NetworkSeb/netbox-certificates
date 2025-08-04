from netbox.views import generic
from django.db.models import Count
from utilities.views import register_model_view

from netbox_certificates.models import CertificateAuthority
from netbox_certificates.forms import CertificateAuthorityForm, CertificateAuthorityFilterForm
from netbox_certificates.tables import CertificateAuthorityTable, CertificateInstanceTable
from netbox_certificates.filtersets import CertificateAuthorityFilterSet

__all__ = (
    "CertificateAuthorityView",
    "CertificateAuthorityListView",
    "CertificateAuthorityEditView",
    "CertificateAuthorityDeleteView",
)

@register_model_view(CertificateAuthority)
class CertificateAuthorityView(generic.ObjectView):
    queryset = CertificateAuthority.objects.all()

    def get_extra_context(self, request, instance):
        table = CertificateInstanceTable(instance.certificates.all())
        table.configure(request)

        return {
            'certificate_table': table
        }

@register_model_view(CertificateAuthority, "list", path="", detail=False)
class CertificateAuthorityListView(generic.ObjectListView):
    queryset = CertificateAuthority.objects.annotate(
        certificate_count = Count('certificates')
    )
    table = CertificateAuthorityTable
    filterset=CertificateAuthorityFilterSet
    filterset_form = CertificateAuthorityFilterForm
    
@register_model_view(CertificateAuthority, "add", detail=False)
@register_model_view(CertificateAuthority, "edit")
class CertificateAuthorityEditView(generic.ObjectEditView):
    queryset = CertificateAuthority.objects.all()
    form = CertificateAuthorityForm

@register_model_view(CertificateAuthority, "delete")
class CertificateAuthorityDeleteView(generic.ObjectDeleteView):
    queryset = CertificateAuthority.objects.all()

# @register_model_view(CertificateAuthority, "bulk_import", detail=False)
# class CertificateAuthorityBulkImportView(generic.BulkImportView):
#     queryset = CertificateAuthority.objects.all()
#     model_form = CertificateAuthorityImportFrom
#     table = CertificateAuthorityTable
#     default_return_url = "plugins:netbox_certificates:certificateauthority_list"

@register_model_view(CertificateAuthority, "bulk_edit", path="edit", detail=False)
class CertificateAuthorityBulkEditView(generic.BulkEditView):
    queryset = CertificateAuthority.objects.all()
    filterset = CertificateAuthorityFilterSet
    table = CertificateAuthorityTable
    form = CertificateAuthorityForm

@register_model_view(CertificateAuthority, "bulk_delete", path="delete", detail=False)
class CertificateAuthorityBulkDeleteView(generic.BulkDeleteView):
    queryset = CertificateAuthority.objects.all()
    filterset = CertificateAuthorityFilterSet
    table = CertificateAuthorityTable
from netbox.views import generic
from django.db.models import Count

from netbox_certificates.models import CertificateInstance
from netbox_certificates.forms import CertificateInstanceForm, CertificateInstanceFilterForm, CertificateInstanceImportFrom
from netbox_certificates.tables import CertificateInstanceTable
from netbox_certificates.filtersets import CertificateInstanceFilterSet

class CertificateInstanceView(generic.ObjectView):
    queryset = CertificateInstance.objects.all()

class CertificateInstanceListView(generic.ObjectListView):
    queryset = CertificateInstance.objects.all()
    table = CertificateInstanceTable
    filterset=CertificateInstanceFilterSet
    filterset_form = CertificateInstanceFilterForm

class CertificateInstanceEditView(generic.ObjectEditView):
    queryset = CertificateInstance.objects.all()
    form = CertificateInstanceForm

class CertificateInstanceDeleteView(generic.ObjectDeleteView):
    queryset = CertificateInstance.objects.all()

class CertificateInstanceBulkImportView(generic.BulkImportView):
    queryset = CertificateInstance.objects.all()
    model_form = CertificateInstanceImportFrom
    table = CertificateInstanceTable
    default_return_url = "plugins:netbox_certificates:certificateinstance_list"
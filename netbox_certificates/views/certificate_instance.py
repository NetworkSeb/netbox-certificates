from netbox.views import generic
from django.db.models import Count

from netbox_certificates.models import CertificateInstance
from netbox_certificates.forms import CertificateInstanceForm
from netbox_certificates.tables import CertificateInstanceTable

class CertificateInstanceView(generic.ObjectView):
    queryset = CertificateInstance.objects.all()

class CertificateInstanceListView(generic.ObjectListView):
    queryset = CertificateInstance.objects.all()
    table = CertificateInstanceTable

class CertificateInstanceEditView(generic.ObjectEditView):
    queryset = CertificateInstance.objects.all()
    form = CertificateInstanceForm

class CertificateInstanceDeleteView(generic.ObjectDeleteView):
    queryset = CertificateInstance.objects.all()

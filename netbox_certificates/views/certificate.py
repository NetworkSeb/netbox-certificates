from netbox.views import generic
from django.db.models import Count

from django.shortcuts import render, get_object_or_404
from netbox_certificates.models import Certificate
from netbox_certificates.forms import CertificateForm
from netbox_certificates.tables import CertificateTable, CertificateInstanceTable

class CertificateView(generic.ObjectView):
    queryset = Certificate.objects.all()

    def get_extra_context(self, request, instance):
        table = CertificateInstanceTable(instance.certificate.all())
        table.configure(request)

        return {
            'instances_table': table
        }

class CertificateListView(generic.ObjectListView):
    queryset = Certificate.objects.annotate(
        instance_count = Count('instances')
    )
    table = CertificateTable

class CertificateEditView(generic.ObjectEditView):
    queryset = Certificate.objects.all()
    form = CertificateForm

class CertificateDeleteView(generic.ObjectDeleteView):
    queryset = Certificate.objects.all()
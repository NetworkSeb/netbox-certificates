from netbox.views import generic

from netbox_certificates.models import CertificateAssignment
from netbox_certificates.forms import CertificateAssignmentForm
from netbox_certificates.tables import CertificateAssignmentTable
from netbox_certificates.filtersets import CertificateAssignmentFilterSet


class CertificateAssignmentListView(generic.ObjectListView):
    queryset = CertificateAssignment.objects.all()
    table = CertificateAssignmentTable
    filterset = CertificateAssignmentFilterSet

class CertificateAssignmentView(generic.ObjectView):
    queryset = CertificateAssignment.objects.all()

class CertificateAssignmentEditView(generic.ObjectEditView):
    queryset = CertificateAssignment.objects.all()
    form = CertificateAssignmentForm

class CertificateAssignmentDeleteView(generic.ObjectDeleteView):
    queryset = CertificateAssignment.objects.all()
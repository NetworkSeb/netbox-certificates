from netbox.views import generic
from django.db.models import Count

from django.shortcuts import render, get_object_or_404
from netbox_certificates.models import Certificate
from netbox_certificates.forms import CertificateForm
from netbox_certificates.tables import CertificateTable

class CertificateView(generic.ObjectView):
    queryset = Certificate.objects.all()

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

# def certificate_list(request):
#     certificates = Certificate.objects.all()
#     return render(request, 'certificate_list.html', {'certificates': certificates})

# def certificate_detail(request, pk):
#     certificate = get_object_or_404(Certificate, pk=pk)
#     return render(request, 'certificate_detail.html', {'certificate': certificate})

# def certificate_instance_list(request):
#     instances = CertificateInstance.objects.all()
#     return render(request, 'certificate_instance_list.html', {'instances': instances})

# def device_certificate_list(request):
#     device_certificates = DeviceCertificate.objects.all()
#     return render(request, 'device_certificate_list.html', {'device_certificates': device_certificates})
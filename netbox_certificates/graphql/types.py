from typing import Annotated, List

import strawberry
import strawberry_django

from netbox.graphql.types import NetBoxObjectType
from tenancy.graphql.types import TenantType, ContactType, ContactGroupType
from dcim.graphql.types import DeviceType
from virtualization.graphql.types import VirtualMachineType

from netbox_certificates.models import (
    Certificate,
    CertificateAuthority,
    CertificateInstance
)

from .filters import (
    NetBoxCertificateFilter,
    NetBoxCertificateInstanceFilter,
    NetBoxCertificateAuthorityFilter,
)

@strawberry_django.type(Certificate, fields="__all__", filters=NetBoxCertificateFilter)
class NetBoxCertificateType(NetBoxObjectType):
    cn: str
    san: str
    device: Annotated["DeviceType", strawberry.lazy("dcim.graphql.types")] | None
    vm: Annotated["VirtualMachineType", strawberry.lazy("virtualization.graphql.types")] | None
    status: str
    type: str
    term: str
    active: Annotated["NetBoxCertificateInstanceType", strawberry.lazy("netbox_certificates.graphql.types")]
    latest: Annotated["NetBoxCertificateInstanceType", strawberry.lazy("netbox_certificates.graphql.types")]
    content: str
    vault_url: str
    fs_cert_location: str
    fs_key_location: str
    install_type: str
    service_commands: str
    service_check: str
    monitor: str
    service_lb: bool
    host_consistent: bool
    automated: bool
    technical_owner: Annotated["ContactType", strawberry.lazy("tenancy.graphql.types")] | None
    technical_group: Annotated["ContactGroupType", strawberry.lazy("tenancy.graphql.types")] | None
    business_contact: Annotated["ContactType", strawberry.lazy("tenancy.graphql.types")] | None
    business_group: Annotated["ContactGroupType", strawberry.lazy("tenancy.graphql.types")] | None
    infrastructure_contact: Annotated["ContactType", strawberry.lazy("tenancy.graphql.types")] | None
    infrastructure_group: Annotated["ContactGroupType", strawberry.lazy("tenancy.graphql.types")] | None

@strawberry_django.type(CertificateInstance, fields="__all__", filters=NetBoxCertificateInstanceFilter)
class NetBoxCertificateInstanceType(NetBoxObjectType):
    ca_reference: str
    ca: Annotated["NetBoxCertificateAuthorityType", strawberry.lazy("netbox_certificates.graphql.types")]
    issuer: str
    pubkey_algorithm: str
    pubkey_size: str
    pubkey_sha1: str
    term: int
    certificate: Annotated["NetBoxCertificateType", strawberry.lazy("netbox_certificates.graphql.types")]
    serial_number: str
    issue_date: str
    expiry_date: str
    status: str
    surpassed: bool
    csr: str
    key: str
    pem: str
    infrastructure_installer: Annotated["ContactType", strawberry.lazy("tenancy.graphql.types")] | None

@strawberry_django.type(CertificateAuthority, fields="__all__", filters=NetBoxCertificateAuthorityFilter)
class NetBoxCertificateAuthorityType(NetBoxObjectType):
    name: str
    acme_url: str
    admin_url: str
    status: str
    cert_profile_ev_id: int
    cert_profile_ov_id: int
    cert_profile_wildcard_id: int
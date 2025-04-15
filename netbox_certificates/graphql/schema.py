from typing import List

import strawberry
import strawberry_django

from .types import (
    NetBoxCertificateType,
    NetBoxCertificateInstanceType,
    NetBoxCertificateAuthorityType,
)

@strawberry.type(name="Query")
class NetBoxCertificateQuery:
    netbox_certificates_certificate: NetBoxCertificateType = strawberry_django.field()
    netbox_certificates_certificate_list: List[NetBoxCertificateType] = (
        strawberry_django.field()
    )

@strawberry.type(name="Query")
class NetBoxCertificateInstanceQuery:
    netbox_certificates_certificateinstance: NetBoxCertificateInstanceType = strawberry_django.field()
    netbox_certificates_certificateinstance_list: List[NetBoxCertificateInstanceType] = (
        strawberry_django.field()
    )

@strawberry.type(name="Query")
class NetBoxCertificateAuthorityQuery:
    netbox_certificates_certificateauthority: NetBoxCertificateAuthorityType = strawberry_django.field()
    netbox_certificates_certificateauthortiy_list: List[NetBoxCertificateAuthorityType] = (
        strawberry_django.field()
    )
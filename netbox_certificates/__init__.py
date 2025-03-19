from netbox.plugins import PluginConfig

class NetBoxCertificatesConfig(PluginConfig):
    name = 'netbox_certificates'
    verbose_name = 'NetBox Certificates'
    description = 'Model and Manage Certificates in Netbox'
    version = '0.0.1'
    base_url = 'certificates'

config = NetBoxCertificatesConfig
from netbox.plugins import PluginConfig

class NetBoxCertificatesConfig(PluginConfig):
    name = 'netbox_certificates'
    description = 'Model and Manage Certificates in Netbox'
    version = '0.0.2'
    author = 'Network Seb'
    base_url = 'certificates'
    verbose_name = 'Netbox Certificates'
    default_settings = {}
    required_settings = []
    min_version = '4.2.0'
    features = ['journaling', 'contact_assignments']
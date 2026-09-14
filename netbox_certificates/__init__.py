from netbox.plugins import PluginConfig

class NetBoxCertificatesConfig(PluginConfig):
    name = 'netbox_certificates'
    verbose_name = 'NetBox Certificates'
    description = 'Model and Manage Certificates in Netbox'
    version = '0.0.2'
    base_url = 'certificates'
    template_extensions = 'template_content.template_extensions'
    api_urls = 'api.urls'

config = NetBoxCertificatesConfig
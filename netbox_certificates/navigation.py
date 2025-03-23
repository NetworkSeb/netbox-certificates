from extras.plugins import PluginMenuItem

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_certificates:certificate_list',
        link_text='Certificates'
    ),
    PluginMenuItem(
        link='plugins:netbox_certificates:certificate_authority_list',
        link_text='Certificate Authorities'
    ),
    PluginMenuItem(
        link='plugins:netbox_certificates:certificate_instance_list',
        link_text='Certificate Instances'
    ),
)
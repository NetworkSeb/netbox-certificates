from netbox.plugins import PluginMenuButton, PluginMenuItem, PluginMenu

# Buttons

certificate_buttons = [
    PluginMenuButton(
        link='plugins:netbox_certificates:certificate_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
    )
]

certificate_authority_buttons = [
    PluginMenuButton(
        link='plugins:netbox_certificates:certificate-authority_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
    )
]

certificate_instance_buttons = [
    PluginMenuButton(
        link='plugins:netbox_certificates:certificate_instance_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
    )
]


menu_items = (
    PluginMenuItem(
        link='plugins:netbox_certificates:certificate_list',
        link_text='Certificates',
        buttons=certificate_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_certificates:certificate-authority_list',
        link_text='Certificate Authorities',
        buttons=certificate_authority_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_certificates:certificate_instance_list',
        link_text='Certificate Instances',
        buttons=certificate_instance_buttons
    ),
)
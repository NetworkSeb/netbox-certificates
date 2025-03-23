from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

# Buttons

certificate_buttons = [
    PluginMenuButton(
        link='plugins:netbox_access_lists:certificate_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

certificate_authority_buttons = [
    PluginMenuButton(
        link='plugins:netbox_access_lists:certificate_authority_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

certificate_instance_buttons = [
    PluginMenuButton(
        link='plugins:netbox_access_lists:certificate_instance_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]


menu_items = (
    PluginMenuItem(
        link='plugins:netbox_certificates:certificate_list',
        link_text='Certificates',
        buttons=certificate_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_certificates:certificate_authority_list',
        link_text='Certificate Authorities',
        buttons=certificate_authority_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_certificates:certificate_instance_list',
        link_text='Certificate Instances',
        buttons=certificate_instance_buttons
    ),
)
from netbox.plugins import PluginMenuButton, PluginMenuItem, PluginMenu

# Buttons

certificate_buttons = [
    PluginMenuButton(
        link='plugins:netbox_certificates:certificate_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
    ),
    PluginMenuButton(
            link="plugins:netbox_certificates:certificate_bulkimport",
            title=("Import"),
            icon_class="mdi mdi-upload",
    ),
]

certificate_authority_buttons = [
    PluginMenuButton(
        link='plugins:netbox_certificates:certificateauthority_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
    )
]

certificate_instance_buttons = [
    PluginMenuButton(
        link='plugins:netbox_certificates:certificateinstance_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
    ),
    PluginMenuButton(
            link="plugins:netbox_certificates:certificateinstance_bulkimport",
            title=("Import"),
            icon_class="mdi mdi-upload",
    ),
]

menu = PluginMenu(
    label='Certificates',
    groups=(
        ('Certificates',
            (
                PluginMenuItem(
                    link='plugins:netbox_certificates:certificate_list',
                    link_text='Certificates',
                    buttons=certificate_buttons
                ),
                PluginMenuItem(
                    link='plugins:netbox_certificates:certificateauthority_list',
                    link_text='Certificate Authorities',
                    buttons=certificate_authority_buttons
                ),
                PluginMenuItem(
                    link='plugins:netbox_certificates:certificateinstance_list',
                    link_text='Certificate Instances',
                    buttons=certificate_instance_buttons
                ),
            ),
        ),
    ),
    icon_class="mdi mdi-certificate-outline",
)
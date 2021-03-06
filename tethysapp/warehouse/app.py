from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import CustomSetting
from tethys_sdk.permissions import Permission, PermissionGroup


class Warehouse(TethysAppBase):
    """
    Tethys app class for Warehouse.
    """

    name = 'Tethys App Warehouse'
    index = 'warehouse:home'
    icon = 'warehouse/images/appicon.png'
    package = 'warehouse'
    root_url = 'warehouse'
    color = '#2b7ac0'
    description = 'The Tethys App Warehouse enables you to discover, install, manage and configure Tethys Applications for your Tethys portal.'
    tags = 'Tethys,Warehouse,Conda,Github'
    enable_feedback = True
    feedback_emails = ["rohitkh@byu.edu"]

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='warehouse',
                controller='warehouse.controllers.home'
            ),
            UrlMap(
                name='get_resources',
                url='warehouse/get_resources',
                controller='warehouse.controllers.get_resources'
            ),
            UrlMap(
                name='install_notifications',
                url='warehouse/install/notifications',
                controller='warehouse.controllers.notificationsConsumer',
                protocol='websocket'
            )
        )

        return url_maps

    def permissions(self):
        """
        Require admin to use the app.
        """
        use_warehouse = Permission(
            name='use_warehouse',
            description='Use the warehouse'
        )

        admin = PermissionGroup(
            name='admin',
            permissions=(use_warehouse,)
        )

        permissions = (admin,)

        return permissions

    def custom_settings(self):
        return (
            CustomSetting(
                name='sudo_server_pass',
                type=CustomSetting.TYPE_STRING,
                description='Sudo password for server',
                required=False
            ),
        )

        return custom_settings

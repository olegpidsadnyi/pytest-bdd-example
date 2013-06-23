from flask.ext.admin import Admin
from flask.ext.admin.base import MenuLink

admin = Admin(
    name='Dashboard',
    url='/',
)

admin.add_link(
    MenuLink(
        name='Logout',
        endpoint='security.logout',
    )
)

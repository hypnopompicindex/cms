from django.utils.translation import ugettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard, AppIndexDashboard


class CustomIndexDashboard(Dashboard):
    columns = 3

    def init_with_context(self, context):
        self.children.append(modules.AppList(
            _('Applications'),
            exclude=('auth.*', 'filebrowser.*', 'globalsettings.*'),
            column=0,
            order=0
        )),
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            20,
            column=1,
            order=0
        ))
        self.children.append(modules.AppList(
            _('Authentication'),
            exclude=('enticemode.*', 'globalsettings.*', 'presentationmode.*', 'kidszone.*', 'mainmenu.*', 'wowmode.*', 'filebrowser.*'),
            column=2,
            order=0
        )),
        self.children.append(modules.LinkList(
            _('File Manager'),
            children=[
                {
                    'title': _('File Manager'),
                    'url': '/admin/filebrowser/browse/',
                    'external': True,
                },
            ],
            column=2,
            order=1
        ))
        self.children.append(modules.LinkList(
            _('Global Settings'),
            children=[
                {
                    'title': 'Content Styling',
                    'url': '/globalsettings/contentstyling/2/change/',
                    'external': True,
                },
                {
                    'title': 'Video Wall',
                    'url': '/globalsettings/videowall/1/change/',
                    'external': True,
                },
                {
                    'title': 'Publish CMS',
                    'url': '/globalsettings/publish/1/change/',
                    'external': True,
                },
            ],
            column=0,
            order=1
        ))
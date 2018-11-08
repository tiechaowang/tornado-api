from tornado.web import url
from apps.api.views.demo import DemoHandler
from apps.api.views.idc import IDCHandler


urlpattern = (
    (r"/", DemoHandler),
    (r"/idc", IDCHandler),
)
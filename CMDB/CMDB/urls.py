from tornado.web import url
#from tornado.web import StaticFileHandler

from apps.api import urls as api_urls

from CMDB.settings import settings

# class MyFileHandler(StaticFileHandler):
#     def write_error(self, status_code, **kwargs):
#         if status_code == 404:
#             self.redirect('http://baidu.com') 

urlpattern = [
    #(url("/", StaticFileHandler, {'path':settings["MEDIA_ROOT"]}))
]


urlpattern += api_urls.urlpattern

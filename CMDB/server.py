from tornado import web
import tornado
from peewee_async import Manager

from CMDB.urls import urlpattern
from CMDB.settings import settings, database

if __name__ == "__main__":

    app = web.Application(urlpattern, debug=True, **settings)
    app.listen(8000)

    objects = Manager(database)
    # No need for sync anymore!
    database.set_allow_sync(False)
    app.objects = objects

    tornado.ioloop.IOLoop.current().start()


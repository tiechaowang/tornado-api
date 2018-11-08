from datetime import datetime
from CMDB.settings import database
from peewee import *


class BaseMode(Model):
    create_date = DateTimeField(default="2015-01-01 00:00:00", null=False, verbose_name="添加时间")
    update_date = DateTimeField(default=datetime.now, null=False, verbose_name="修改时间")

    last_editor = CharField(default="", max_length=32, verbose_name="最后修改人")

    class Meta:
        database = database

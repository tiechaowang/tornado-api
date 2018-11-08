import json, time
from apps.api.models import Idc
from utils.base_handlers import BaseHandler


class IDCHandler(BaseHandler):
    model_name = Idc

    async def get(self):

        return await super(IDCHandler, self).get()

    async def post(self):
        return await super(IDCHandler, self).post()

    async def put(self):

        return await super(IDCHandler, self).put()

    async def delete(self):

        return await super(IDCHandler, self).delete()
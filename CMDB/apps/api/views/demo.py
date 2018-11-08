import json, time
from apps.api.models import TestNameModel
from utils.base_handlers import BaseHandler
from utils.base_filter import common_filter


class DemoHandler(BaseHandler):
    model_name = TestNameModel
    # async def get(self):
    #     request_param = json.loads(self.request.body)
    #     result = {}
    #     result["data"] = []
    #     result["current_page"] = request_param["current_page"]
    #     offset = int(request_param["page_row"]) * (int(request_param["current_page"])-1)
    #     data_filter = common_filter(TestNameModel, request_param["filter_data"])
    #     # data_filter = TestNameModel.select()
    #     # for filter_condition in  request_param["filter_data"]:
    #     #     if filter_condition["column"] == "id":
    #     #         if filter_condition["condition"] == "in":
    #     #             data_filter = data_filter.filter(eval("TestNameModel.id") << filter_condition["content"].split(","))
    #     #         if filter_condition["condition"] == "equel":
    #     #             data_filter = data_filter.filter(TestNameModel.id == filter_condition["content"])
    #     total = await self.application.objects.count(data_filter)
    #     data_filter = data_filter.offset(offset).limit(int(request_param["page_row"]))
    #     data_list = await self.application.objects.execute(data_filter)
    #     result["total"] = total
    #     for object_model in data_list:
    #         result["data"].append(object_model.tojson())
    #     self.finish(json.dumps(result))

    # async def post(self):
    #     request_param = json.loads(self.request.body)
    #     obj = await self.application.objects.create(TestNameModel, name=request_param.get("name"))
    #     self.finish("add success")

    # async def put(self):
    #     request_param = json.loads(self.request.body)
    #     obj = await self.application.objects.get(TestNameModel, id=int(request_param.get("id")))
    #     obj.name = request_param.get("name")
    #     await self.application.objects.update(obj)
    #     self.finish("update success")

    # async def delete(self):
    #     request_param = json.loads(self.request.body)
    #     obj = await self.application.objects.get(TestNameModel, id=int(request_param.get("id")))
    #     await self.application.objects.delete(obj)
    #     self.finish("delete success")
from tornado.web import RequestHandler
import json
from utils.base_filter import common_filter
from utils.base_param_validate import validate_get_param, validate_action_param
from utils.base_model_column_validate import validate_model_get_param, validate_model_post_param, validate_model_action_param


class BaseHandler(RequestHandler):
    model_name = None
    def set_default_headers(self):
        self.set_header('Content-type', 'application/json')

    def options(self, *args, **kwargs):
        pass

    async def get(self):
        try:
            result = validate_get_param(self.request.body)
            if result.get("flag") == "1":
                return self.finish(json.dumps(result))
            result = validate_model_get_param(self.model_name, self.request.body)
            if result.get("flag") == "1":
                return self.finish(json.dumps(result))

            result["data"] = []
            request_param = json.loads(self.request.body)
            result["current_page"] = request_param["current_page"]
            offset = int(request_param["page_row"]) * (int(request_param["current_page"])-1)
            data_filter = common_filter(self.model_name, request_param["filter_data"])
            total = await self.application.objects.count(data_filter)
            data_filter = data_filter.offset(offset).limit(int(request_param["page_row"]))
            data_list = await self.application.objects.execute(data_filter)
            result["total"] = total
            for object_model in data_list:
                result["data"].append(object_model.tojson())
            self.finish(json.dumps(result))
        except Exception as e:
            result["flag"] = "1"
            result["msg"] = str(e)
            self.finish(json.dumps(result))

    async def post(self):
        try:
            result = validate_action_param(self.request.body)
            if result.get("flag") == "1":
                return self.finish(json.dumps(result))
            result = validate_model_post_param(self.model_name, self.request.body)
            if result.get("flag") == "1":
                return self.finish(json.dumps(result))

            request_param = json.loads(self.request.body)
            data = request_param["data"]
            obj = await self.application.objects.create(self.model_name, **data)
            self.finish(json.dumps(result))
        except Exception as e:
            result["flag"] = "1"
            result["msg"] = str(e)
            self.finish(json.dumps(result))

    async def put(self):
        try:
            result = validate_action_param(self.request.body)
            if result.get("flag") == "1":
                return self.finish(json.dumps(result))

            result = validate_model_action_param(self.model_name, self.request.body)
            if result.get("flag") == "1":
                return self.finish(json.dumps(result))

            request_param = json.loads(self.request.body)
            obj = await self.application.objects.get(self.model_name, id=int(request_param.get("data").get("id")))
            del request_param.get("data")["id"]
            for key,value in request_param.get("data").items():
                exec("obj.%s = '%s'" %(key, value))
            await self.application.objects.update(obj)
            self.finish(json.dumps(result))
        except Exception as e:
            result["flag"] = "1"
            result["msg"] = str(e)
            self.finish(json.dumps(result))

    async def delete(self):
        try:
            result = validate_action_param(self.request.body)
            if result.get("flag") == "1":
                return self.finish(json.dumps(result))

            result = validate_model_action_param(self.model_name, self.request.body)
            if result.get("flag") == "1":
                return self.finish(json.dumps(result))

            request_param = json.loads(self.request.body)
            obj = await self.application.objects.get(self.model_name, id=int(request_param.get("data").get("id")))
            await self.application.objects.delete(obj)
            self.finish(json.dumps(result))
        except Exception as e:
            result["flag"] = "1"
            result["msg"] = str(e)
            self.finish(json.dumps(result))
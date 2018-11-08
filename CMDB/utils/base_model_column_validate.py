import json

def validate_model_get_param(model_name, params):
    result = {"flag": "0"}
    request_param = json.loads(params)
    model_column = model_name().tojson().keys()
    filter_list = request_param.get("filter_data")

    for param in filter_list:
        if param.get("column") not in model_column:
            result["msg"] = "%s not find" % param.get("column")
            result["flag"] = "1"
        if param.get("condition") not in ["in", "like", "equal"]:
            result["msg"] = "%s not support, column: %s" % (param.get("condition"), param.get("column"))
            result["flag"] = "1"
        if param.get("content") == "" or param.get("content") == None:
            result["msg"] = "content not '', column: %s" % (param.get("column"))
            result["flag"] = "1"
    return result

def validate_model_post_param(model_name, params):
    result = {"flag": "0"}
    request_param = json.loads(params)
    model_column = model_name().tojson().keys()
    filter_list = request_param.get("data").keys()

    for param in filter_list:
        if param not in model_column:
            result["msg"] = "column %s not find" % param
            result["flag"] = "1"

    # if len(model_column) != (len(filter_list)+1):
    #     result["flag"] = "1"
    #     result["msg"] = "total column count not equal model column"
    return result

def validate_model_action_param(model_name, params):
    result = {"flag": "0"}
    request_param = json.loads(params)
    model_column = model_name().tojson().keys()
    filter_list = request_param.get("data").keys()
    for param in filter_list:
        if param not in model_column:
            result["msg"] = "column %s not find" % param
            result["flag"] = "1"
    return result

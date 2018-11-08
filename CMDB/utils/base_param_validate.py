import json

def validate_get_param(params):
    result = {}
    result["flag"] = "0"
    request_param = json.loads(params)
    if request_param.get("current_page") is None:
        result["msg"] = "current_page param not find"
        result["flag"] = "1"
    else:
        try:
            int(request_param.get("current_page"))
        except Exception as e:
            result["msg"] = "current_page value  not int"
            result["flag"] = "1"
    if request_param.get("filter_data") is None:
        result["msg"] = "filter_data param not find"
        result["flag"] = "1"
    else:
        if type(request_param.get("filter_data")) == list:
            for param in request_param.get("filter_data"):
                if type(param) != dict:
                    result["flag"] = "1"
                    esult["msg"] = "filter_data content must is dict"
                    break
        else:
            result["msg"] = "filter_data param must is list"
            result["flag"] = "1"
    if request_param.get("page_row") is None:
        result["msg"] = "page_row param not find"
        result["flag"] = "1"
    else:
        try:
            int(request_param.get("page_row"))
        except Exception as e:
            result["msg"] = "page_row value  not int"
            result["flag"] = "1"
    if request_param.get("token") is None:
        result["msg"] = "token param not find"
        result["flag"] = "1"
    if request_param.get("flag") is None:
        result["msg"] = "flag param not find"
        result["flag"] = "1"
    else:
        if request_param.get("flag") not in ["0", "1"]:
            result["msg"] = "flag param must string 0 or 1"
            result["flag"] = "1"
    return result


def validate_action_param(params):
    result = {}
    result["flag"] = "0"
    request_param = json.loads(params)
    if request_param.get("data") is None:
        result["msg"] = "data param not find"
        result["flag"] = "1"
    else:
        if type(request_param.get("data")) != dict:
            result["msg"] = "data param must is dict"
            result["flag"] = "1"
    if request_param.get("token") is None:
        result["msg"] = "token param not find"
        result["flag"] = "1"
    if request_param.get("flag") is None:
        result["msg"] = "flag param not find"
        result["flag"] = "1"
    else:
        if request_param.get("flag") not in ["0", "1"]:
            result["msg"] = "flag param must string 0 or 1"
            result["flag"] = "1"
    return result

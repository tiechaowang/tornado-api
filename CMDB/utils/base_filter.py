from apps.api.models import * 

def common_filter(model_name, filter_column_list):
    model_str = model_name.__name__
    data_filter = model_name.select()
    for filter_column in filter_column_list:
        if filter_column["condition"] == "in":
            data_filter = data_filter.filter(eval("%s.%s" % (model_str, filter_column["column"])) << filter_column["content"].split(","))
        if filter_column["condition"] == "equal":
            data_filter = data_filter.filter(eval("%s.%s" % (model_str, filter_column["column"])) == filter_column["content"])
        if filter_column["condition"] == "like":
            content = "%" +  filter_column["content"] + "%"
            data_filter = data_filter.filter(eval("%s.%s" % (model_str, filter_column["column"])) ** content)
    return data_filter

import requests, json, time, subprocess, datetime
import base64,re

#r=requests.get("http://ip:port/",data=json.dumps({"current_page":"1", 
#    "filter_data":[{"content": "1,2,3,4", "condition": "in", "column": "id"}], "page_row": "2", "token": "", "flag": "0"}))

#r=requests.get("http://ip:port/",data=json.dumps({"current_page":"1", 
#    "filter_data":[{"content": "test", "condition": "like", "column": "name"}], "page_row": "2", "token": "", "flag": "0"}))

#r=requests.post("http://ip:port/",data=json.dumps({"data": {"name":"test one"}, "token": "", "flag": "0"}))

#r=requests.put("http://ip:port/",data=json.dumps({"data": {"id":"1","name":"test"}, "token": "", "flag": "0"}))

#r=requests.delete("http://ip:port/",data=json.dumps({"data": {"id":"1"}, "token": "", "flag": "0"}))

print(r.text)

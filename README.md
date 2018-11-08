tornado-api
===========
this is tornado asynchronous  project  for High concurrency design databse fast encapsulation api

Environmental
-------------

* aiomysql == 0.0.19
* peewee == 3.7.1
* peewee-async == 0.5.12
* PyMySQL == 0.9.2
* tornado == 5.1.1
* requests == 2.20.0


Initial data
-------

python CMDB/tools/init_db.py


run
-------

cd CMDB
python server.py


test api
-------

r=requests.get("http://ip:port/",data=json.dumps({"current_page":"1", "filter_data":[{"content": "1,2,3,4", "condition": "in", "column": "id"}], "page_row": "2", "token": "", "flag": "0"}))

r=requests.get("http://ip:port/",data=json.dumps({"current_page":"1", "filter_data":[{"content": "test", "condition": "like", "column": "name"}], "page_row": "2", "token": "", "flag": "0"}))

r=requests.post("http://ip:port/",data=json.dumps({"data": {"name":"test one"}, "token": "", "flag": "0"}))

r=requests.put("http://ip:port/",data=json.dumps({"data": {"id":"1","name":"test"}, "token": "", "flag": "0"}))

r=requests.delete("http://ip:port/",data=json.dumps({"data": {"id":"1"}, "token": "", "flag": "0"}))



License
-------

The code itself is released to the public domain for people quick start.

The example files  is  wangtiechao corresponding license.

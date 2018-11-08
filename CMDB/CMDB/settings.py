import os

import peewee_async

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
settings = {
   
}

database = peewee_async.MySQLDatabase(
    'CMDB_dev', host="10.132.2.43", port=3306, user="root", password="123.com"
)


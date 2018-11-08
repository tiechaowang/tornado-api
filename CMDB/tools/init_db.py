from CMDB.settings import database
from apps.api.models import *


def init():
    database.create_tables([TestNameModel, Os, Idc, Oem, Rack, Device, Vm, App, Accessories, Map, Ips, Ip])


if __name__ == "__main__":
    init()


#show create table oem;show create table os;show create table idc;show create table rack;show create table ips;show create table ip;show create table device;show create table vm;show create table app; show create table accessories; show create table map;
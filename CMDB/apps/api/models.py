from peewee import *
from datetime import datetime
from utils.base_models import BaseMode


class TestNameModel(BaseMode):
    name = CharField(null=False)

    def __str__(self):
        return self.name

    def tojson(self):
        return {"name": self.name}


class Map(BaseMode):
    """
    map公司-项目-平台路由表
    """
    company = CharField(default="", null=False, max_length=64, verbose_name="公司")
    project = CharField(default="", null=False, max_length=64, verbose_name="项目")
    platform = CharField(default="", null=False, max_length=64, verbose_name="平台")
    op_owner = CharField(default="", null=False, max_length=32, verbose_name="运维负责人")
    dev_owner = CharField(default="", null=False, max_length=32, verbose_name="研发负责人")

class Os(BaseMode):
    """
    操作系统表
    """
    os_tuple = (
        (0, u'6.8'),
        (1, u'6.9'),
        (2, u'7.2'),
        (3, u'7.4'),
        (4, u'2003'),
        (5, u'2008'),
        (6, u'2012'),
    )
    arch_tuple = ((0, 64), (1, 32))
    os_oem = CharField(default="", null=False, max_length=16, verbose_name="操作系统厂商")
    os_version = CharField(default=0, null=False, choices=os_tuple, verbose_name="操作系统版本")
    os_arch = CharField(default=0, null=False, choices=arch_tuple, verbose_name="操作系统版本")

class Idc(BaseMode):
    """
    机房表
    """
    status_tuple = (
        (0, u'已启用'),
        (1, u'已停用'),
    )
    arch_tuple = ((0, 64), (1, 32))
    isp = CharField(default="", null=False, max_length=16, verbose_name="运营商")
    line = CharField(default="", null=False, max_length=16, verbose_name="运营商线路")
    bandwidth = CharField(default="", null=False, max_length=16, verbose_name="机房出口带宽")
    racks = IntegerField(default=0, null=False, verbose_name="机柜个数")  # tinyint(4) 代表最小显示位数 无法控制
    city = CharField(default="", null=False, max_length=16, verbose_name="机房城市位置")
    position = CharField(default="", null=False, max_length=32, verbose_name="机房详细位置")
    telephone = CharField(default="", null=False, max_length=16, verbose_name="机房联系电话")
    status = CharField(default=0, null=False, choices=status_tuple, verbose_name="状态")

    def tojson(self):
        return {"id": self.id, "isp": self.isp, "line": self.line, "bandwidth": self.bandwidth, "racks": self.racks, "city": self.city,
            "position": self.position, "telephone": self.telephone, "status": self.status, "create_date": str(self.create_date),
             "update_date": str(self.update_date), "last_editor": self.last_editor}

class Oem(BaseMode):
    """
    厂商表
    """
    asset_type_list = (
        (0, u'服务器'),
        (1, u'交换机'),
        (2, u'防火墙'),
        (3, u'存储设备'),
        (4, u'安全设备'),
    )
    oem = CharField(default="", null=False, max_length=16, verbose_name="厂商")
    asset_type = CharField(default=0, null=False, choices=asset_type_list, verbose_name="设备类型")
    model = CharField(default="", null=False, max_length=16, verbose_name="设备型号")

class Rack(BaseMode):
    """
    机柜表
    """
    status_list = ((0, u'已启用'), (1, u'已停用'))
    idc_id = ForeignKeyField(Idc, verbose_name="机房id")
    name = CharField(default="", null=False, max_length=32, verbose_name="机柜号")
    height = CharField(default="", null=False, max_length=16, verbose_name="机柜高度")
    power = CharField(default="13A", null=False, max_length=16, verbose_name="机柜电力")
    status = CharField(default=0, null=False, choices=status_list, verbose_name="状态")

class Device(BaseMode):
    """
    物理设备表
    """
    sec_area_list = (
        (0, u'inside'),
        (1, u'outside'),
        (2, u'dmz'),
        (3, u'db'),
        (4, u'hadoop'),
    )
    status_list = (
        (0, u'上架'),
        (1, u'下架'),
        (2, u'故障'),
    )
    rent_list = (
        (0, u'未借'),
        (1, u'借出'),
    )
    oem_id = ForeignKeyField(Oem, verbose_name=" 厂商id")
    idc_id = ForeignKeyField(Idc, verbose_name=" 机房id")
    rack_id = ForeignKeyField(Rack, verbose_name="机柜id")
    os_id = ForeignKeyField(Os, verbose_name="操作系统id")
    map_id = ForeignKeyField(Map, verbose_name="路由表id")
    ip1 = IntegerField(default='', null=False, unique=True)  # int(11) 代表最小显示位数 无法控制
    mac1 = CharField(default="00:00:00:00:00:00", null=False, unique=True, max_length=32)
    ip2 = IntegerField(default='', null=False, unique=True)  # int(11) 代表最小显示位数 无法控制
    mac2 = CharField(default="00:00:00:00:00:00", null=False, unique=True, max_length=32)
    ip3 = IntegerField(default='', null=False, unique=True)  # int(11) 代表最小显示位数 无法控制
    mac3 = CharField(default="00:00:00:00:00:00", null=False, unique=True, max_length=32)
    zjxl_sn = CharField(default="", unique=True, null=False, max_length=16, verbose_name="中交兴路资产编号")
    sn = CharField(default="", unique=True, null=False, max_length=16, verbose_name="sn号")
    code = CharField(default="", null=False, unique=True, max_length=16, verbose_name="快速服务器代码")
    config = CharField(default="", max_length=128, verbose_name="服务器配置")
    sec_area = CharField(default=0, null=False, choices=sec_area_list, verbose_name="业务安全域")
    switch_ip = CharField(default="", null=False, max_length=16, verbose_name="设备所连交换机IP地址")
    switch_port = CharField(default="", null=False, max_length=16, verbose_name="设备所连交换机端口")
    salt_id = CharField(default="", null=False, max_length=64)
    buy_time = DateTimeField(default="2015-01-01 00:00:00", null=False, verbose_name="购买时间")
    expiration_time = DateTimeField(default="2015-01-01 00:00:00", null=False, verbose_name="过保时间")
    Renewal_first = DateTimeField(default="2015-01-01 00:00:00", null=False, verbose_name="第一次续保时间")
    Renewal_expiration = DateTimeField(default="2015-01-01 00:00:00", null=False, verbose_name="第一次续保过保时间")
    status = CharField(default=0, null=False, choices=status_list, verbose_name="状态")
    rent = CharField(default=0, null=False, choices=rent_list, verbose_name="设备借用状态")


class Vm(BaseMode):
    """
    虚拟机表
    """
    vm_type_list = (
        (0, u'Openstack'),
        (1, u'Vmware'),
        (2, u'Docker'),
        (3, u'阿里云'),
    )
    status_list = (
        (0, u'空闲'),
        (1, u'上架'),
        (2, u'下架'),
        (3, u'故障'),
    )
    sec_area_list = (
        (0, u'inside'),
        (1, u'outside'),
        (2, u'dmz'),
        (3, u'db'),
        (4, u'hadoop'),
    )
    idc_id = ForeignKeyField(Idc, verbose_name=" 机房id")
    rack_id = ForeignKeyField(Rack, verbose_name="机柜id")
    os_id = ForeignKeyField(Os, verbose_name="操作系统id")
    device_id = ForeignKeyField(Device, verbose_name="物理设备id")
    map_id = ForeignKeyField(Map, null=False, verbose_name="路由表id")
    vm_type = CharField(default=0, null=False, choices=vm_type_list, verbose_name="虚机类型")
    ip1 = IntegerField(default='', null=False, unique=True)  # int(11) 代表最小显示位数 无法控制
    mac1 = CharField(default="00:00:00:00:00:00", null=False, max_length=32)
    ip2 = IntegerField(default='', null=False, unique=True)  # int(11) 代表最小显示位数 无法控制
    mac2 = CharField(default="00:00:00:00:00:00", null=False, max_length=32)
    vm_sn = CharField(default="", null=False, max_length=16, unique=True, verbose_name="虚拟机资产编号")
    status = CharField(default=0, null=False, choices=status_list, verbose_name="状态")
    salt_id = CharField(default="", null=False, max_length=64)
    sec_area = CharField(default=0, null=False, choices=sec_area_list, verbose_name="业务安全域")

class App(BaseMode):
    """
    应用资产表
    """
    status_list = (
        (0, u'备机'),
        (1, u'生产'),
        (2, u'测试'),
        (3, u'开发'),
        (4, u'故障'),
    )
    device_id = ForeignKeyField(Device, null=False, verbose_name="物理设备id")
    map_id = ForeignKeyField(Idc, null=False, verbose_name="映射表id")
    main = CharField(default="", null=False, max_length=16, verbose_name="主类")
    sub1 = CharField(default="", null=False, max_length=16, verbose_name="分类1")
    app_version = CharField(default="", null=False, max_length=16, verbose_name="应用版本")
    app_port = CharField(default="", null=False, max_length=16, verbose_name="应用端口")
    app_path = CharField(default="", null=False, max_length=64, verbose_name="应用部署路径")
    os = CharField(default="", null=False, max_length=16, verbose_name="操作系统版本")
    vip = CharField(default="", null=False, max_length=16, verbose_name="虚拟IP地址")
    status = CharField(default=0, null=False, choices=status_list, verbose_name="状态")

class Accessories(BaseMode):
    """
    配件表
    """
    accessories_type_list = (
        (0, u'CPU'),
        (1, u'内存'),
        (2, u'硬盘'),
        (3, u'网卡'),
    )
    serial_number = CharField(default="", null=False, max_length=64, unique=True, verbose_name="配件序列号")
    accessories_oem = CharField(default="", null=False, max_length=16, verbose_name="配件厂商")
    accessories_type = CharField(default='', null=False, choices=accessories_type_list, verbose_name="配件类型")
    accessories_conf = CharField(default="", null=False, max_length=16, verbose_name="配件配置")
    link_device = CharField(default="", null=False, max_length=16, verbose_name="关联使用主机")


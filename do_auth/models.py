from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Firm(models.Model):
    name = models.CharField(max_length=20, null=False)
    is_active = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    info = models.TextField(default=None, null=True)


class Licence(models.Model):
    """
    firm_user:厂商名称
    creater:创建者，是哪个系统用户创建的该licence
    way:限制方式，0表示用次数限制，1表示用持续时间限制
    source:算法原包路径，指定用户能使用的原包。原包数量可以多个，以字符串存储，提取后做处理。
    limit:限制值。整型。当way为0时，表示可成功完成包的次数，每成功完成1次就减少1，直到为0，
        当way为1时，表示能使用的时间，从create开始算，以小时为基本单位
    is_active:指明该licence是否使用，可以由管理员删除，也可以在使用限制过期后，系统修改为False
    create_time:创建时间
    info:适当备注
    lic:licence值，以前方所有信息和作为源数据，计算出来的MD5值，后面发送给厂商使用，用来登录
    """
    WAY_CHOICE = (
        (0, 'times'),
        (1, 'duration'),
    )
    firm_user = models.ForeignKey(Firm, on_delete=models.CASCADE)
    creater = models.ForeignKey(User, on_delete=models.CASCADE)
    way = models.IntegerField(choices=WAY_CHOICE)
    source = models.TextField(default=None, null=True)
    limit = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    info = models.TextField(default=None, null=True)
    lic = models.CharField(max_length=32, null=False)



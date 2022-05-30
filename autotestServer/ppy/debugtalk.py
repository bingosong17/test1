import time
import os
import sys
import datetime
from dateutil.relativedelta import relativedelta
from importlib import reload
from envAll import envPPYApp, pointInRegion, lonLat
import random
from ppyApp.api.获取当前用户资料_test import TestCase获取当前用户资料 as ppyApp登陆凭证验证脚本
from ppyApp.api.账号验证码登录_test import TestCase账号验证码登录 as ppyApp获取登陆凭证
from wlApp.api.司机详情_test import TestCase司机详情 as wlApp登陆凭证验证脚本
from wlApp.api.司机端登录_test import TestCase用户登陆 as wlApp获取登陆凭证
from kfht.api.获取已登录用户的信息_test import TestCase获取已登录用户的信息 as kfht登陆凭证验证脚本
from kfht.api.客服登录_test import TestCase用户登陆 as kfht获取登陆凭证
from gysht.api.已有供应品牌列表_test import TestCase已有供应品牌列表 as gysht登陆凭证验证脚本
from gysht.api.用户登陆_test import TestCase用户登陆 as gysht获取登陆凭证
from yyht.订单中心.api.全部订单列表_test import TestCase全部订单列表 as yyht登陆凭证验证脚本
from yyht.用户登陆_test import TestCase用户登陆 as yyht获取登陆凭证
from ppApp.api.查询基础数据_test import TestCase查询基础数据 as ppApp登陆凭证验证脚本
from ppApp.业务脚本.拼拼登录_test import TestCase拼拼登录 as ppApp获取登陆凭证
import env
from ppyApp.业务脚本.用户删除购物车商品_test import TestCase用户清空购物车 as 用户清空购物车
from ppApp.api.私海店铺查询_test import TestCase私海店铺查询 as 私海店铺查询
from ppApp.api.公海列表查询_test import TestCase公海列表查询 as 公海列表查询
from ppApp.api.检查打卡条件是否满足_test import TestCase检查打卡条件是否满足 as 检查打卡条件是否满足


def testEnv(business, tag=None):
    """
    根据业务线，返回测试url
    :param business: 业务线
    :param tag: 为线上准备的标志符，目前没用
    :return:
    """
    envlist = [business, env.env]
    if envlist[0] == "yyht":
        """运营后台地址"""
        return "https://web.dev2.pinpianyi.cn/{}_t".format(envlist[1])
    if envlist[0] == "pd":
        """车辆派单地址"""
        return "https://webapi.{}.pinpianyi.cn".format(envlist[1])
    if envlist[0] == "gysht":
        """供应商地址"""
        return "https://gyapi.{}.pinpianyi.cn/ppy-supplier-api".format(envlist[1])
    if envlist[0] == "kfht":
        """客服后台地址"""
        return "https://kfapi.{}.pinpianyi.cn".format(envlist[1])
    if envlist[0] == "ppyApp":
        """ppy app 地址"""
        return "https://gateway.{}.pinpianyi.cn/ppy-mall".format(envlist[1])
    if envlist[0] == "wlApp":
        """物流app地址"""
        return "https://wuliu.{}.pinpianyi.cn".format(envlist[1])
    if envlist[0] == "ppApp":
        """拼拼app地址"""
        return "https://gateway.{}.pinpianyi.cn/ppy-pinpin".format(envlist[1])


def timeStr(name="test"):
    """
    以时间为随机变量，生成名字
    :return: 字符串
    """
    t = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    strings = name + t[-5:-1]
    return strings


def wlversion():
    """
    物流app接口参数需要传入版本号
    :return: 版本号
    """
    return "2.13.2"


def hapentime(hours, type=0, timeType="h"):
    """
    :param timeType: 时间增加类型s/h/d分别为秒、时，天
    :param type: 返回类型
    :param hours:时间数值
    :return: 时间字符串
    """
    if type == 0:
        time_style = '%Y-%m-%d %H:%M'
    elif type == 1:
        time_style = '%Y-%m-%d'
    elif type == 2:
        time_style = '%Y-%m-%d %H:%M:%S'
    elif type == 3:
        time_style = '%Y-%m'
    else:
        raise ValueError("格式参数输入不正确，请修改")

    if timeType == "h":
        timade = (datetime.datetime.now() + relativedelta(hours=int(hours))).strftime(time_style)
    elif timeType == "s":
        timade = (datetime.datetime.now() + relativedelta(seconds=int(hours))).strftime(time_style)
    elif timeType == "d":
        timade = (datetime.datetime.now() + relativedelta(days=int(hours))).strftime(time_style)
    elif timeType == "y":
        timade = (datetime.datetime.now() + relativedelta(years=int(hours))).strftime(time_style)
    elif timeType == "mon":
        timade = (datetime.datetime.now() + relativedelta(months=int(hours))).strftime(time_style)
    elif timeType == "min":
        timade = (datetime.datetime.now() + relativedelta(minutes=int(hours))).strftime(time_style)
    else:
        raise ValueError("时间参数不正确，请修改")
    return str(timade)


def makeGoodPoint(region):
    """
    返回一个区域内的某一有效经纬坐标，并写入文件中，供getLongitude(),getLatitude()函数调用
    :param region: 坐标区域
    """
    file_path = FindFilePath("envAll/lonLat.py")
    res = pointInRegion.checkPointInRegions([region])
    s = "longitude = " + str(res[0]) + "\n" + "latitude = " + str(res[1])
    with open(file_path, "w", encoding='utf-8') as f:
        f.write(s)


def getLongitude():
    """
    返回经度
    :return:
    """
    reload(lonLat)
    return lonLat.longitude


def getLatitude():
    """
    返回纬度
    :return:
    """
    reload(lonLat)
    return lonLat.latitude


def sleep_N_secs(n_secs):
    """
    sleep n seconds after request
    """
    time.sleep(n_secs)


def assert_equal(a, b):
    """
    :param a: 实际值
    :param b: 期望值
    """
    assert str(a) == str(b), "期望数据为{}，实际数据为{}".format(b, a)


def assert_not_equal(a, b):
    """
    :param a: 实际值
    :param b: 期望值
    """
    assert a != b, "期望数据为{}，实际数据为{}".format(b, a)


def assert_contains(body, *args, allIn=1, **kwargs):
    """
    :param allIn: 存在多个比较的时候，1，所有内容均找到则成功。0，有一个找到则成功
    :param body: 原值
    """
    if allIn:
        if args:
            # 如果是元组格式
            for i in args:
                if str(i) not in str(body):
                    raise ValueError("期待值:{}  不在实际值中".format(i))
        if kwargs:
            # 如果body是[{"a":1},{"b":2}]这种类型，kwargs中的值在一个dict中匹配完全，不跨dict匹配
            if isinstance(body, list) and isinstance(body[0], dict):
                tag = 0
                for item in body:
                    tag_dic = 0
                    for key in kwargs.keys():
                        kwargs[key] = dealParmsType(kwargs[key])
                        if item[key] == kwargs[key]:
                            tag_dic += 1
                    if tag_dic == len(kwargs):
                        tag = 1
                if tag == 0:
                    raise ValueError("期待值:{}  不在实际值中".format(kwargs))

    else:
        tag = 0
        if args:
            for i in args:
                if str(i) in str(body):
                    tag = 1
            if tag == 0:
                raise ValueError("期待值:{}  均不在实际值中".format(args))
        if kwargs:
            # 如果body是[{"a":1},{"b":2}]这种类型
            if isinstance(body, list) and isinstance(body[0], dict):
                tag = 0
                for item in body:
                    tag_dic = 0
                    for key in kwargs.keys():
                        kwargs[key] = dealParmsType(kwargs[key])
                        if item[key] == kwargs[key]:
                            tag_dic += 1
                    if tag_dic != 0:
                        tag = 1
                if tag == 0:
                    raise ValueError("期待值:{}  不在实际值中".format(kwargs))


def assert_not_contains(body, *args, **kwargs):
    """
    :param body: 原值
    """
    if args:
        # 如果是元组格式
        for i in args:
            if str(i) in str(body):
                raise ValueError("期待值:{}  在实际值中".format(i))
    if kwargs:
        # 如果body是[{"a":1},{"b":2}]这种类型，kwargs中的值在一个dict中匹配完全，不跨dict匹配
        if isinstance(body, list) and isinstance(body[0], dict):
            tag = 0
            for item in body:
                tag_dic = 0
                for key in kwargs.keys():
                    kwargs[key] = dealParmsType(kwargs[key])
                    if item[key] != kwargs[key]:
                        tag_dic += 1
                if tag_dic == len(kwargs):
                    tag = 1
            if tag == 0:
                raise ValueError("期待值:{}  存在部分/全部在实际值中".format(kwargs))

    pass


def assert_pageDataLength(body, num):
    """
    获取body列表的长度，并与num比较是否相等
    :param num: 预期长度值
    :param body: 返回的列表
    """
    body_lenth = len(body)
    assert body_lenth == int(num), "列表长度为{}，期望长度为{}".format(body_lenth, num)


def exportJsonValue(jsonData, key):
    """
    在一个json内容中，寻找键值为key的值
    :param jsonData: 原数据
    :param key: 要寻找值的键值
    :return: 值
    """
    return jsonData[key]


def exportValue(body, valueKey, **kwargs):
    """
    从字典组成的列表数据中，通过额外的键值对来定位数据，返回valueKey对应的value
    :param body: 字典组成的列表数据，要搜索的数据
    :param valueKey: 需要返回的数据的Key
    :param kwargs: 键值对，用来定位数据
    :return: valueKey对应的value
    """
    if kwargs:
        # 如果body是[{"a":1},{"b":2}]这种类型，kwargs中的值在一个dict中匹配完全，不跨dict匹配
        if isinstance(body, list) and isinstance(body[0], dict):
            for item in body:
                tag_dic = 0
                for key in kwargs.keys():
                    kwargs[key] = dealParmsType(kwargs[key])
                    if item[key] == kwargs[key]:
                        tag_dic += 1
                if tag_dic == len(kwargs):
                    return item[valueKey]
            raise ValueError("未找到您需要的值，请再次确认，内容值为：{},寻找值为：{}".format(body, valueKey))
        raise TypeError("处理数据需要是字典组成的列表格式，您的格式暂未支持，请联系开发")
    raise ValueError("您需要指定额外的键值对来搜索字典，请输入")


def dealParmsType(parm):
    """
    httprunner引用debugtalk中的函数，传参中带有特殊符号函数处理逻辑异常，函数不报错。
    即当需要传入参数为数字字符串时，传："123"，则函数逻辑异常，传入：123，函数当作int
    值处理。此为httprunner框架bug，为处理该问题，定义该函数解决。
    当需要传入参数为数字字符串时，传：strType123，函数解析成"123"供下一个函数使用。
    :param parm:
    """
    if "Type" in str(parm):
        s = str(parm).split("Type")
        if s[0] == "str":
            parm = str(s[1])
        elif s[0] == "int":
            parm = int(s[1])
        else:
            pass
    return parm


def FindFilePath(filename):
    """
    由于脚本调用debugtalk中的函数，执行路径变为脚本所在的路径。debugtalk里面的函数如果涉及到文件
    读取，文件写入，文件存在路径丢失情况。所以以此函数，一级一级向上寻找读写的文件的绝对路径，便于
    操作，并将目录存放到sys.path中，便于调用函数
    :param filename: 要寻找路径的文件名字
    :return: 返回文件的绝对路径
    """
    path = os.path.abspath(__file__)
    while True:
        if os.path.exists(path + "/" + filename):
            sys.path.insert(0, path)
            return path + "/" + filename
        if path == "/":
            return False
        path = os.path.dirname(path)


def verifyToken(classObj, user_id, business):
    """
    验证记录的登陆凭证是否有效，如果有效返回使用
    :param business: 业务线
    :param classObj: 验证脚本
    :param user_id: 用户唯一标志符
    :return: 有效凭证，或者False
    """
    reload(envPPYApp)
    try:
        # 如果列表中只有一个数（第一个和最后一个相等），说明不是物流，按照通常处理
        if envPPYApp.token[user_id][0] == envPPYApp.token[user_id][-1]:
            classA = classObj()
            # 考虑到有的验证脚本需要的token,有的需要session，这里两个都传，保证不错
            classA.config.variables(**{
                "business": business,
                "token": envPPYApp.token[user_id][0],
                "session": envPPYApp.token[user_id][0],
                "session_yyht": envPPYApp.token[user_id][0],
            })
            return envPPYApp.token[user_id][0]
        else:  # 列表存在两个数，说明是物流，需要传如userId
            classA = classObj()
            classA.config.variables(**{
                "business": business,
                "token": envPPYApp.token[user_id][0],
                "userId": envPPYApp.token[user_id][1],
            })
            classA.test_start()
            return envPPYApp.token[user_id][0]
    except:
        return False


def updateToken(classObj, phone, user_id, business):
    """
    更新或生成新的有效的token，返回并记录
    :param business: 业务线
    :param classObj: 生成token脚本
    :param phone: 登陆号码
    :param user_id: 用户唯一标志符
    :return: 登陆凭证
    """
    reload(envPPYApp)
    # token无效两种情况，第一种是超时，第二种是不存在，需要分别处理
    path_envPPYApp = FindFilePath("envAll/envPPYApp.py")
    if user_id in envPPYApp.token.keys():
        # 如果是存在token，过期了，先删除这条记录
        with open(path_envPPYApp, encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if user_id in line:
                    lines.remove(line)
                    break
            s = ''.join(lines)
        with open(path_envPPYApp, "w", encoding='utf-8') as f:
            f.write(s)
    classB = classObj()
    classB.config.variables(
        **{
            "business": business,
            "phone": phone,
        }
    )
    classB.test_start()
    variables = classB.get_export_variables()
    try:
        # 查看返回中，有没有userId，有的话说明是物流app
        with open(path_envPPYApp, encoding='utf-8') as f:
            lines = f.readlines()
            strings = "'" + user_id + "' : ['" + variables['session'] + "','" + str(variables['userId']) + "'],\n"
            lines.insert(1, strings)  # 插入第二行
            s = ''.join(lines)
    except:
        # 文档直接写入方式保存token
        with open(path_envPPYApp, encoding='utf-8') as f:
            lines = f.readlines()
            strings = "'" + user_id + "' : ['" + variables['session'] + "'],\n"
            lines.insert(1, strings)  # 插入第二行
            s = ''.join(lines)

    with open(path_envPPYApp, "w", encoding='utf-8') as f:
        f.write(s)
    return variables['session']


def getSession(business, phone=None):
    """
    读取系统是否保存有效的登陆凭证 ，如果没有，调用登陆脚本，在文件中写入有效的登陆凭证
    :param business: 业务线
    :param phone: 用户手机号码
    :return: token值
    """
    # 如果业务线为yyht，直接从env环境中读取登陆号码，简化脚本编写，否则，检测不得为空
    if business == 'yyht' or business == 'pd':
        phone = env.phone
    else:
        if phone is None:
            print("phone值不能为空")
            exit()
    envs = env.env
    cityCode = env.cityCode
    # 使用环境，城市和电话号码，生成一个唯一的user_id作为key保存token
    user_id = envs + cityCode + phone
    env_dic = {
        "ppyApp": [ppyApp登陆凭证验证脚本, ppyApp获取登陆凭证],
        "wlApp": [wlApp登陆凭证验证脚本, wlApp获取登陆凭证],
        "kfht": [kfht登陆凭证验证脚本, kfht获取登陆凭证],
        "gysht": [gysht登陆凭证验证脚本, gysht获取登陆凭证],
        "yyht": [yyht登陆凭证验证脚本, yyht获取登陆凭证],
        "pd": [yyht登陆凭证验证脚本, yyht获取登陆凭证],
        "ppApp": [ppApp登陆凭证验证脚本, ppApp获取登陆凭证],
    }

    # 使用一个简单的ppyApp脚本，验证token的有效性
    if business in env_dic.keys():
        result = verifyToken(env_dic[business][0], user_id, business)
        if result:
            return result
        else:
            return updateToken(env_dic[business][1], phone, user_id, business)
    else:
        print("业务线不在范围内")


def getWlAppUserId(phone):
    reload(envPPYApp)
    user_id = env.env + env.cityCode + phone
    return envPPYApp.token[user_id][1]


def makeList(*args):
    """
    将元素生成list返回
    :param args: 元素
    :return:
    """
    lis = []
    for item in args:
        lis.append(item)
    return lis


def getPageDataToList(body, key):
    """
    处理pagedata类型数据，提取key对应的值，处理成列表返回
    :param body: 字典的列表组合
    :param key: 提取value对应的key
    """
    lis = []
    for item in body:
        lis.append(item[key])
    return lis


def modifyPageData(body, **kwargs):
    # ADDlogisticsArea=strType3310001
    for key in kwargs:
        print("要处理的值{}".format(key))
        if key.startswith("ADD"):
            value = dealParmsType(kwargs[key])
            for item in body:
                item[key[3:]] = value
    return body


def 清空用户购物车(phone):
    classA = 用户清空购物车()
    classA.config.variables(
        **{
            "business": "ppyApp",
            "phone": phone,
            "token": "${getSession($business,$phone)}",
        }
    )
    try:
        while classA.test_start():
            pass
    except:
        pass


def createRandomString(length=6):
    """
    @功能：     生成一个随机字符串，默认6位
    @para:
    length: 随机数位数，默认为6位
    @return: 返回一个包含大小写字母和数字的字符串
    :param length:
    :return:
    """
    code_list = []
    for i in range(10):  # 0-9数字
        code_list.append(str(i))
    for i in range(65, 91):  # A-Z
        code_list.append(chr(i))
    for i in range(97, 123):  # a-z
        code_list.append(chr(i))
    myslice = random.sample(code_list, length)  # 从list中随机获取6个元素，作为一个片断返回
    random_string = ''.join(myslice)  # list to string
    return random_string


def createRandomNumber(length=7):
    """
    @功能：     生成一个随机数字字符串
    @para:
    length: 随机数位数，默认为15位
    @return: 返回一串一定位数数字组成的字符串
    已有更好的随机数方法，Interface.XianSuoApp.JiFenShangCheng.XsJiFenShangChengIntf.createRandomNumber
    :param length:
    :return:
    """
    if length <= 0:
        print("参数错误，请输入正整数")
        return -1
    else:
        loop = length // 10
        code_list = []
        for i in range(loop + 1):
            for i in range(10):  # 0-9数字
                code_list.append(str(i))
    myslice = random.sample(code_list, length)
    random_number = ''.join(myslice)  # list to string
    return random_number


#  生成随机手机号
"""
phone:生成18开头的随机11位手机号,例：1812345678
pwd:生成随机字母加数字的字符串，例：YUNhj12345
"""


def get_only_data(type='phone'):
    import random, time, string
    if type == "phone":
        middle_num = "".join(random.choice("0123456789") for i in range(7))  # 随机取7个数
        right = str(int(time.time())).split('.')[0][-2:]  # 时间戳后两位
        return "{}{}{}".format("18", middle_num, right)

    elif type == 'pwd':
        num = string.ascii_letters + string.digits
        return "".join(random.sample(num, 10))


def 拼拼公私海店铺生成个未拜访的店铺id(phone, types=0, status=1):
    if types == 0:
        classA = 私海店铺查询()
    else:
        classA = 公海列表查询()
    classA.config.variables(
        **{
            "business": "ppApp",
            "phone": phone,
            "session": "${getSession($business,$phone)}",
            "status": status,
            "pageSize": 100,
            "longitude": "",
            "latitude": "",
            "manyDayNotOrder": 0,
            "userSignStatus": 0,
            "type": "1",
            "manyDayNotLogin": 0,
        }
    )
    classA.test_start()
    variables = classA.get_export_variables()

    for item in variables['pageData']:
        classB = 检查打卡条件是否满足()
        classB.config.variables(
            **{
                "business": "ppApp",
                "phone": phone,
                "session": "${getSession($business,$phone)}",
                "shopId": item["id"]
            }
        )

        classB.test_start()
        var = classB.get_export_variables()
        if var["check_value"] == 2000:
            return item["id"]
        elif var["check_value"] == 6200:
            raise EnvironmentError("/visitRecord/queryVisitRecord 接口无响应，请查看环境")
        else:
            print("已经拜访过的id:" + str(item["id"]))
            continue

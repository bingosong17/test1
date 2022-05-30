# NOTE: Generated By HttpRunner v3.1.3
"""
    概要：
        新派物流中为订单派车
    输入参数：
        "phone": 运营后台登陆账号
        "pass": 运营后台登陆密码
        "orderNo": 订单号,
        "cityCode": 城市编号,
        "phoneToWl": 司机手机号
        "plannedStartTime": 派车时间
    输出参数：

    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.物流中心.新派物流.api.查询待派订单列表_test import TestCase查询待派订单列表 as 查询待派订单列表
from yyht.物流中心.新派物流.api.新增车辆订单信息_test import TestCase新增车辆订单信息 as 新增车辆订单信息
from yyht.物流中心.新派物流.api.修改虚拟运单车型_test import TestCase修改虚拟运单车型 as 修改虚拟运单车型
from yyht.物流中心.新派物流.api.根据ID查询虚拟运单信息_test import TestCase根据Id查询虚拟运单信息 as 根据Id查询虚拟运单信息
from yyht.物流中心.新派物流.api.单个生成运单_test import TestCase单个生成运单 as 单个生成运单
from yyht.物流中心.新派物流.api.根据车型查看司机信息_test import TestCase根据车型查看司机信息 as 根据车型查看司机信息
from yyht.物流中心.新派物流.api.查询路径规划计算状态_test import TestCase查询路径规划计算状态 as 查询路径规划计算状态
from yyht.物流中心.运力管理.api.查询司机列表_test import TestCase查询司机列表 as 查询司机列表



class TestCase订单派车(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "",
            "session": "${getSession($business)}",
            "orderNo": "2020081315204511614765",
            "phoneToWl": "13738113393",
            "plannedStartTime": "${hapentime(2)}"

        })

    teststeps = [
        Step(
            RunTestCase("查询司机列表").call(查询司机列表).export(*["driverId","vehicleType"])
        ),
        Step(
            RunTestCase("查询待派订单列表").call(查询待派订单列表)
        ),
        Step(
            RunTestCase("新增车辆订单信息").call(新增车辆订单信息)
                .export(*["tempDistributeId", "virtualTransportationId", "uuid"])
                .teardown_hook("${sleep_N_secs(2)}")
        ),
        Step(
            RunTestCase("查询路径规划计算状态").call(查询路径规划计算状态)
                .teardown_hook("${sleep_N_secs(4)}")
        ),
        Step(
            RunTestCase("根据车型查看司机信息").call(根据车型查看司机信息)
        ),
        Step(
            RunTestCase("修改虚拟运单车型").call(修改虚拟运单车型)
                .teardown_hook("${sleep_N_secs(2)}")
        ),
        Step(
            RunTestCase("根据ID查询虚拟运单信息").call(根据Id查询虚拟运单信息)
                .teardown_hook("${sleep_N_secs(2)}")
        ),
        Step(
            RunTestCase("生成运单").call(单个生成运单)
        ),
    ]


if __name__ == "__main__":
    TestCase订单派车().test_start()

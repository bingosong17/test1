"""
    概要：
        司机完成取货送货流程
    输入参数：
        "phone": 运营后台登陆账号
        "pass": 运营后台登陆密码
        "orderNo": 订单号,
        "cityCode": 城市编号,
    输出参数：
        无
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from wlApp.业务脚本.司机完成运单fast_test import TestCase取送货 as 完成取送货
from yyht.物流中心.运单管理.业务脚本.通过订单获取运单id_test import TestCase通过订单获取运单id as 通过订单获取运单id


class TestCase司机完成运单(HttpRunner):

    config = Config("testcase description").verify(False)\
        .variables(
        **{
            "transOrderId": 2011261231803811397141917,
        }
    )

    teststeps = [
        Step(
            RunTestCase("通过订单获取运单id").call(通过订单获取运单id)
            .export(*["transOrderId", "phoneNumber"])
        ),
        Step(
            RunTestCase("完成取送货").call(完成取送货)
        ),
    ]


if __name__ == "__main__":
    TestCase司机完成运单().test_start()


"""
    概要：
        将已经生效的订单派车，生成运单且生效（只考虑一运单只包含一个订单情况）
    输入参数：
        "phone": 运营后台登陆账号
        "pass": 运营后台登陆密码
        "orderNo": 订单号,
        "cityCode": 城市编号,
        "phoneToWl": 司机号码
        "plannedStartTime": 派车时间
    输出参数：
        无
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.物流中心.新派物流.业务脚本.订单派车fast_test import TestCase订单派车 as 订单派车
from yyht.物流中心.运单管理.业务脚本.使指定订单的运单生效_test import TestCase运单生效 as 运单生效
import env


class TestCase订单生成运单(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "pd",
            "orderNo": "2020101220073317518253",
            "phoneToWl": "13738113393",
            "plannedStartTime": "${hapentime(2)}"
        })

    teststeps = [
        Step(
            RunTestCase("订单派车").call(订单派车).teardown_hook("${sleep_N_secs(2)}")
        ),
        Step(
            RunTestCase("运单生效").call(运单生效)
        ),
    ]


if __name__ == "__main__":
    TestCase订单生成运单().test_start()


# NOTE: Generated By HttpRunner v3.1.3
"""
      概要：
        修改私海店铺信息
    输入参数：
       "phone": 登陆用户手机号码
    输出参数：
        无
    前置接口：
        用户登陆；获取私海列表；店铺修改
"""

from httprunner import HttpRunner, Config, Step, RunTestCase
from ppApp.业务脚本.查询私海列表 import TestCase查询私海列表 as 查询私海列表
from ppApp.api.店铺修改_test import TestCase店铺修改 as 店铺修改


class TestCase店铺修改私海(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "ppApp",
            "phone": "15869038912",
            "session": "${getSession($business,$phone)}",
        })

    teststeps = [
        Step(
            RunTestCase("查询私海列表").call(查询私海列表).export(*["shopId"])
        ),
        Step(
            RunTestCase("店铺修改").call(店铺修改)
        )
    ]


if __name__ == "__main__":
    TestCase店铺修改私海().test_start()


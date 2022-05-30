# -*- coding: utf-8 -*-
"""
    概要：
        新增会员商品校验
    输入参数：
        "env":
        "session":
    输出参数：
       msg
    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.营销中心.api.新增会员商品_test import TestCase新增会员商品 as 新增会员商品
import env


class TestCase新增会员商品校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
                "startTime": "2020-09-19 00:00:00",
                "endTime": "2020-10-31 00:00:00",
                "goodsId": 37,
        })

    teststeps = [
        Step(
            RunTestCase("新增会员商品").call(新增会员商品).export(*["msg"])
            .teardown_hook("${assert_contains($msg,'已经是会员商品')}")
        ),
    ]


if __name__ == "__main__":
    TestCase新增会员商品校验().test_start()

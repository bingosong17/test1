#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/20 10:08
"""
    概要：
       红包停用校验
    输入参数：
        "env":
        "session":
    输出参数：
        $statusCode
    前置接口：
        用户登陆
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase, client
from yyht.营销中心.业务脚本.新增新人礼包红包_test import TestCase新增新人礼包红包 as 新增新人礼包红包
from yyht.营销中心.api.红包列表_test import TestCase红包列表 as 红包列表
from yyht.营销中心.api.红包停用_test import TestCase红包停用 as 红包停用
import env


class TestCase新增会员商品校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",

        })

    teststeps = [
        Step(
            RunTestCase("新增新人礼包红包").call(新增新人礼包红包)
        ),
        Step(
            RunTestCase("红包列表").call(红包列表).export("packetId")
        ),
        Step(
            RunTestCase("红包停用").call(红包停用)
        ),

    ]


if __name__ == "__main__":
    TestCase新增会员商品校验().test_start()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/27 11:03
"""
    概要：
      在售商品搜索校验，输入搜索条件，验证搜索结果是否正确
    输入参数：

    输出参数：

    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.商品中心.api.在售商品查询_test import TestCase在售商品查询 as 在售商品查询
class TestCase在售商品搜索校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "queryValue": 53095,
        })

    teststeps = [

        Step(
            RunTestCase("在售商品查询").call(在售商品查询).export(*["goodsId"])
            .teardown_hook("${assert_equal($goodsId,None)}")
        ),

    ]


if __name__ == "__main__":
    TestCase在售商品搜索校验().test_start()

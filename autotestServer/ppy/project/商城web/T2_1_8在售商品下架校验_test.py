#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/27 11:53
"""
    概要：
      在售商品搜索校验，校验上下架接口是否通过
    输入参数：
        "id": "$id",  非商品id   列表id
        "type": -1,  商品上下加架，-1  表示下架
    输出参数：

    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.商品中心.api.在售商品查询_test import TestCase在售商品查询 as 在售商品查询
from yyht.商品中心.api.商品上下架_test import TestCase商品上下架 as 商品上下架
class TestCase在售商品搜索校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "type": -1,
        })

    teststeps = [

        Step(
            RunTestCase("在售商品查询").call(在售商品查询).export(*["id"])
        ),
        Step(
            RunTestCase("商品上下架").call(商品上下架)
        ),
        Step(
            RunTestCase("在售商品查询").call(在售商品查询).export(*["disabled"])
            .teardown_hook("${assert_equal($disabled, '0'}")
        ),

    ]


if __name__ == "__main__":
    TestCase在售商品搜索校验().test_start()

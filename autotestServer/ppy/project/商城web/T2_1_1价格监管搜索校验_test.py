#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/21 10:17
"""
    概要：
      点击搜索，查看这个规则在列表中是否存在
    输入参数：
        无
    输出参数：
        msg
    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.商品中心.api.毛利锁规则列表_test import TestCase毛利锁规则列表 as 毛利锁规则列表

class TestCase价格监管搜索校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
        })

    teststeps = [
        Step(
            RunTestCase("毛利锁规则列表").call(毛利锁规则列表).export(*["pageData"])
            .teardown_hook("${assert_contains($pageData,ruleId)}")
        ),
    ]


if __name__ == "__main__":
    TestCase价格监管搜索校验().test_start()

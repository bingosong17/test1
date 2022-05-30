#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/22 16:42
"""
    概要：
        查看毛利锁规则明细接口校验
    输入参数：
         ruleId 毛利锁规则ID
        status  启用状态 1启用
    输出参数：
        msg
    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.商品中心.api.毛利锁规则列表_test import TestCase毛利锁规则列表 as 毛利锁规则列表
from yyht.商品中心.api.查询毛利锁规则明细_test import TestCase查询毛利锁规则明细 as 查询毛利锁规则明细

class TestCase价格监管搜索校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
        })
    teststeps = [
        Step(
            RunTestCase("毛利锁规则列表").call(毛利锁规则列表).export(*["ID"])
        ),
        Step(
            RunTestCase("查询毛利锁规则明细").with_variables(
                **{
                    "ruleId": "$ID",
                }
            ).call(查询毛利锁规则明细).export(*["ruleId"])
            .teardown_hook("${assert_equal($ruleId,$ID)}")
        ),
    ]


if __name__ == "__main__":
    TestCase价格监管搜索校验().test_start()

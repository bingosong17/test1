#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/22 15:50
"""
    概要：
      毛利锁规则启用停用校验，查看列表数据状态
      先查询数据是停用状态，再启用，然后再停用，可确保每次都可以跑通过
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
from yyht.商品中心.api.价格监管规则停用_test import TestCase价格监管规则停用 as 价格监管规则停用

class TestCase启用停用毛利说规则校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "mngStatusTo214": [1],
        })

    teststeps = [
        Step(
            RunTestCase("毛利锁规则列表").with_variables(
                **{
                    "mngStatus": "$mngStatusTo214",
                }
            ).call(毛利锁规则列表).export(*["ruleId"])
        ),
        Step(
            RunTestCase("价格监管规则停用").with_variables(
                **{
                    "ruleId": "$ruleId",
                    "status": 3,
                }
            ).call(价格监管规则停用)
        ),
        Step(
            RunTestCase("毛利锁规则列表").with_variables(
                **{
                    "mngStatus": [3],
                }
            ).call(毛利锁规则列表).export(*["pageData"])
            .teardown_hook("${assert_contains($pageData,ruleId=intType$ruleId)}")
        ),
        Step(
            RunTestCase("价格监管规则启用").with_variables(
                **{"status": 1}
            )
            .call(价格监管规则停用)
        ),
    ]


if __name__ == "__main__":
    TestCase启用停用毛利说规则校验().test_start()

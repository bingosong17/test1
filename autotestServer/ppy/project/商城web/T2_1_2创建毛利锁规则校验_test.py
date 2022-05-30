#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/22 15:00
"""
    概要：
      新增毛利锁规则，列表查看是否新增成功，掉删除接口是为了每次都可以新增，不然规则只能新增一个
    输入参数：
        ruleName 规则名称
    输出参数：
        "ruleName", 规则名称
        "statusText", 规则状态
        "ruleId" 规则ID
    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.商品中心.api.创建毛利锁规则_test import TestCase创建毛利锁规则 as 创建毛利锁规则
from yyht.商品中心.api.毛利锁规则列表_test import TestCase毛利锁规则列表 as 毛利锁规则列表
from yyht.商品中心.api.删除毛利锁规则_test import TestCase删除毛利锁规则 as 删除毛利锁规则

class TestCase价格监管搜索校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "startTime": "${hapentime(1)}"+":00",
            "endTime": "${hapentime(100)}"+":00",
            "ruleName": "毛利锁2",
            "mngStatusTo212": [0],
        })

    teststeps = [
        Step(
            RunTestCase("创建毛利锁规则").call(创建毛利锁规则)
        ),
        Step(
            RunTestCase("毛利锁规则列表").with_variables(
                **{
                    "mngStatus": "$mngStatusTo212",
                }
            ).call(毛利锁规则列表).export(*["ruleName", "statusText", "ruleId"])
            .teardown_hook("${assert_equal($ruleName,毛利锁2)}")
        ),
        Step(
            RunTestCase("删除毛利锁规则").call(删除毛利锁规则)
        ),
    ]


if __name__ == "__main__":
    TestCase价格监管搜索校验().test_start()

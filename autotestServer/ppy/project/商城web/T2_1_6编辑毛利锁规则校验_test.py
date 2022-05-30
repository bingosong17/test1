#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/22 17:15
"""
    概要：
        编辑毛利锁信息，将强管控改为弱管控
    输入参数：
         ruleId 毛利锁规则ID
        status  启用状态 1启用
        handleType  超限处理方式 1强管控2弱管控需审核
    输出参数：
        msg
    前置接口：
        用户登陆
"""
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.商品中心.api.毛利锁规则列表_test import TestCase毛利锁规则列表 as 毛利锁规则列表
from yyht.商品中心.api.查询毛利锁规则明细_test import TestCase查询毛利锁规则明细 as 查询毛利锁规则明细
from yyht.商品中心.api.编辑毛利锁规则_test import TestCase编辑毛利锁规则 as 编辑毛利锁规则


class TestCase价格监管搜索校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "handleType": 1,
        })
    teststeps = [
        Step(
            RunTestCase("毛利锁规则列表").call(毛利锁规则列表).export(*["ID"])
        ),
        Step(
            RunTestCase("编辑毛利锁规则").call(编辑毛利锁规则)
        ),
        Step(
            RunTestCase("查询毛利锁规则明细").call(查询毛利锁规则明细).export(*["handleType"])
            .teardown_hook("${assert_equal($handleType,1)}")
        ),
    ]


if __name__ == "__main__":
    TestCase价格监管搜索校验().test_start()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/27 17:27
"""
    概要：
        新增新人礼包，列表页B环校验
    输入参数：

    输出参数：
        $packetName： 会员红包名称
    前置接口：
        用户登陆
"""
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase, client
from yyht.营销中心.业务脚本.新增新人礼包_test import TestCase新增新人礼包 as 新增新人礼包
from yyht.营销中心.api.新人礼包列表_test import TestCase新人礼包列表 as 新人礼包列表

class TestCase新增新人礼包校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "packetName": "新人礼包红包",
        })

    teststeps = [
        Step(
            RunTestCase("新增新人礼包").call(新增新人礼包)
        ),
        Step(
            RunTestCase("新人礼包列表").call(新人礼包列表).export(*["pageData"])
            .teardown_hook("${assert_contains($pageData,bagName,新人礼包)}")
        ),

    ]


if __name__ == "__main__":
    TestCase新增新人礼包校验().test_start()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/24 14:37
"""
    概要：
        新增会员红包成功，审核红包列表显示该条数据
    输入参数：
        "env":
        "session":
    输出参数：
        $packetName： 会员红包名称
    前置接口：
        用户登陆
"""
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase, client
from yyht.营销中心.api.新增会员红包_test import TestCase新增会员红包 as 新增会员红包
from yyht.营销中心.api.红包列表_test import TestCase红包列表 as 红包列表



class TestCase新增会员红包校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "availableStartTime": "${hapentime(1)}"+":00",
            "availableEndTime":  "${hapentime(100)}"+":00",
            "packetName": "会员红包5块5",

        })

    teststeps = [
        Step(
            RunTestCase("新增会员红包").call(新增会员红包)
        ),
        Step(
            RunTestCase("红包列表").call(红包列表).export(*["pageData"])
            .teardown_hook("${assert_contains($pageData,packetName=$packetName)}")
        ),

    ]


if __name__ == "__main__":
    TestCase新增会员红包校验().test_start()

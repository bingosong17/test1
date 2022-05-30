#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/20 13:56
"""
    概要：
        新增icon校验
    输入参数：
        "env":
        "session":
    输出参数：
        iconName： icon名称
    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.营销中心.api.新增icon_test import TestCase新增Icon as 新增icon
from yyht.营销中心.api.icon列表_test import TestCaseIcon列表 as icon列表
import env


class TestCase新增icon校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
        })

    teststeps = [
        Step(
            RunTestCase("新增icon").call(新增icon)
        ),
        Step(
            RunTestCase("icon列表").call(icon列表).export(*["iconName"])
            .teardown_hook("${assert_equal($iconName,test_郑小和)}")
        ),
    ]


if __name__ == "__main__":
    TestCase新增icon校验().test_start()

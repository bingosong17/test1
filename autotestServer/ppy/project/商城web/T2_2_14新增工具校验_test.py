#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/20 11:42
"""
    概要：
        新增工具校验
    输入参数：
        "env":
        "session":
    输出参数：
        $toolName： 工具名称
    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.营销中心.api.新增tool_test import TestCase新增Tool as 新增toll
from yyht.营销中心.api.tool列表_test import TestCaseTool列表 as tool列表
import env


class TestCase新增工具校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "toolName": "test_工具",
        })

    teststeps = [
        Step(
            RunTestCase("新增toll").call(新增toll)
        ),
        Step(
            RunTestCase("tool列表").call(tool列表).export(*["toolName"])
            .teardown_hook("${assert_equal($toolName,“test_工具”)}")
        ),
    ]


if __name__ == "__main__":
    TestCase新增工具校验().test_start()

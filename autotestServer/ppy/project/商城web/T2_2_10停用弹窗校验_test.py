#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/20 17:20
"""
    概要：
        弹窗停用
    输入参数：
        "env":
        "session":
    输出参数：
        msg
    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.营销中心.api.弹窗停用_test import TestCase弹窗停用 as 弹窗停用
import env


class TestCase弹窗停用校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
        })

    teststeps = [
        Step(
            RunTestCase("弹窗停用").call(弹窗停用).export(*["msg"])
            .teardown_hook("${assert_contains($msg,'未查询到该弹框信息')}")
        ),
    ]


if __name__ == "__main__":
    TestCase弹窗停用校验().test_start()

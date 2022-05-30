#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/20 15:35
"""
    概要：
        新增弹窗校验
    输入参数：
        "env":
        "session":
        "windowName": "弹窗名称,
    输出参数：
        $windowName： 弹窗名称,
    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.营销中心.api.新增弹窗_test import TestCase新增弹窗 as 新增弹窗
from yyht.营销中心.api.弹窗列表_test import TestCase弹窗列表 as 弹窗列表
import env


class TestCase新增弹窗校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "windowName": "弹窗_郑小和",
            "startTime": "${hapentime(1)}" + ":00",
            "endTime": "${hapentime(100)}" + ":00",
        })

    teststeps = [
        Step(
            RunTestCase("新增弹窗").call(新增弹窗)
        ),
        Step(
            RunTestCase("弹窗列表").call(弹窗列表).export(*["windowName"])
            .teardown_hook("${assert_equal($windowName,弹窗_郑小和)}")
        ),
    ]


if __name__ == "__main__":
    TestCase新增弹窗校验().test_start()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/20 14:28
"""
    概要：
        新增专题校验
    输入参数：
        "env":
        "session":
    输出参数：
        topicName： 专题名称
    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.营销中心.api.新增专题_test import TestCase新增专题 as 新增专题
from yyht.营销中心.api.专题搜索_test import TestCase专题搜索 as 专题搜索
import env


class TestCase新增icon校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "startTime": "${hapentime(1)}" + ":00",
            "endTime": "${hapentime(100)}" + ":00",
            "topicName": "专题_郑小和",
        })

    teststeps = [
        Step(
            RunTestCase("新增专题").call(新增专题)
        ),
        Step(
            RunTestCase("专题搜索").call(专题搜索).export(*["topicName"])

            .teardown_hook("${assert_equal($topicName,专题_郑小和)}")
        ),
    ]


if __name__ == "__main__":
    TestCase新增icon校验().test_start()

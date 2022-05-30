#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/20 16:08
"""
    概要：
        删除广告校验
    输入参数：
        "env":
        "session":
    输出参数：
        msg
    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.营销中心.api.新增广告_test import TestCase新增广告 as 新增广告
from yyht.营销中心.api.广告列表_test import TestCase广告列表 as 广告列表
from yyht.营销中心.api.删除广告_test import TestCase删除广告 as 删除广告
import env


class TestCase删除广告校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "startTime": "${hapentime(1)}"+":00",
            "endTime": "${hapentime(100)}"+":00",
        })

    teststeps = [
        Step(
            RunTestCase("新增i广告").call(新增广告)
        ),
        Step(
            RunTestCase("广告列表").call(广告列表).export(*["launchName", "launchId"])
            .teardown_hook("${assert_equal($launchName,广告_郑小和)}")
        ),
        Step(
            RunTestCase("删除广告").with_variables(

            ).call(删除广告)
        ),
    ]


if __name__ == "__main__":
    TestCase删除广告校验().test_start()


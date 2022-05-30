#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/20 16:27
"""
    概要：
        新增背景图校验
    输入参数：
        "env":
        "session":
    输出参数：
        $backgroundImageName： 背景图名称,
    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.营销中心.api.新增背景图_test import TestCase新增背景图 as 新增背景图
from yyht.营销中心.api.背景图列表_test import TestCase背景图列表 as 背景图列表
from yyht.营销中心.api.删除背景图_test import TestCase删除背景图 as 删除背景图



class TestCase新增背景图校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "startTime": "${hapentime(1)}" + ":00",
            "endTime": "${hapentime(100)}" + ":00",
        })

    teststeps = [
        Step(
            RunTestCase("新增背景图").call(新增背景图)
        ),
        Step(
            RunTestCase("背景图列表").call(背景图列表).export(*["backgroundImageName", "backgroundImageId"])
            .teardown_hook("${assert_equal($backgroundImageName,背景图_郑小和)}")
        ),
        Step(
            RunTestCase("删除背景图").call(删除背景图)
        ),
    ]


if __name__ == "__main__":
    TestCase新增背景图校验().test_start()


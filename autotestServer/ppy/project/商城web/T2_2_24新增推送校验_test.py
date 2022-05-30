#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/19 10:57
"""
    概要：
        新增推送消息，查看消息列表是否新增推送
    输入参数：
         "pushFlag": 1,是否发送push.1是2否
            "showFlag": 1,站内是否显示。1是2否
            "name“：消息名称
    输出参数：
        "name“：消息名称
    前置接口：
        无
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.营销中心.api.新增推送_test import TestCase新增推送 as 新增推送
from yyht.营销中心.api.推送消息列表_test import TestCase推送消息列表 as  推送消息列表
import random


class TestCase新增推送校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "failureFlag": 1,
            "pushFlag": 1,
            "showFlag": 1,
            "name": "我是消息推送",
        })

    teststeps = [
        Step(
            RunTestCase("新增推送").call(新增推送)
        ),
        Step(
            RunTestCase("推送消息列表").call(推送消息列表).export(*["name"])
            .teardown_hook("${assert_equal($name, 杭州站_我是消息推送)}")
        ),
    ]


if __name__ == "__main__":
    TestCase新增推送校验().test_start()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/27 16:52
"""
    概要：
        新增新人礼包
    输入参数：

    输出参数：
        packetId ：红包ID

    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.营销中心.业务脚本.新增新人礼包红包_test import TestCase新增新人礼包红包 as 新增新人礼包红包
from yyht.营销中心.api.新增新人礼包_test import TestCase新增新人礼包 as 新增新人礼包

class TestCase新增新人礼包(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "packetName": "新人礼包红包",
        })

    teststeps = [
        Step(
            RunTestCase("新增新人礼包红包").call(新增新人礼包红包).export(*["packetId"])
            .teardown_hook("${sleep_N_secs(2)}")
        ),
        Step(
            RunTestCase("新增新人礼包").with_variables(
                **{
                    "packetIds": ["$packetId"]
                }
            ).call(新增新人礼包)
            .teardown_hook("${sleep_N_secs(2)}")
        ),

    ]


if __name__ == "__main__":
        TestCase新增新人礼包().test_start()

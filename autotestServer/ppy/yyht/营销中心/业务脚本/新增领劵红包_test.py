#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/19 11:34
"""
    概要：
        新增领劵红包
    输入参数：
        "packetName": "领劵红包",红包名称
    输出参数：
        packetId ：红包ID
    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.营销中心.api.新增领劵红包_test import TestCase新增领劵红包 as 新增领劵红包
from yyht.营销中心.api.红包列表_test import TestCase红包列表 as 红包列表
from yyht.营销中心.api.获取红包审核信息详情_test import TestCase获取红包审核信息详情 as 获取红包审核信息
from yyht.营销中心.api.审核红包_test import TestCase审核红包 as 审核红包


class TestCase新增领劵红包(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "packetName": "领劵红包",
        }).export(*["packetId"])

    teststeps = [
        Step(
            RunTestCase("新增领劵红包").call(新增领劵红包).teardown_hook("${sleep_N_secs(2)}")
        ),
        Step(
            RunTestCase("红包列表").call(红包列表).export(*["packetId"])
            .teardown_hook("${sleep_N_secs(2)}")
        ),
        Step(
            RunTestCase("获取红包审核信息").call(获取红包审核信息).teardown_hook("${sleep_N_secs(2)}")
        ),
        Step(
            RunTestCase("审核红包").call(审核红包).teardown_hook("${sleep_N_secs(2)}")
        ),
    ]


if __name__ == "__main__":
    TestCase新增领劵红包().test_start()


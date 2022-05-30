#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/19 11:54
"""
    概要：
        新增领劵红包成功，审核红包列表显示该条数据
    输入参数：
        "env":
        "session":
    输出参数：
        $packetName： 会员红包名称
    前置接口：
        用户登陆
"""
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase, client
from yyht.营销中心.api.新增领劵红包_test import TestCase新增领劵红包 as 新增领劵红包
from yyht.营销中心.api.红包审核列表_test import TestCase红包审核列表 as 红包审核列表
import env


class TestCase新增领劵红包校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "packetName": "领劵红包",

        })

    teststeps = [
        Step(
            RunTestCase("新增领劵红包").call(新增领劵红包)
        ),
        Step(
            RunTestCase("红包审核列表").call(红包审核列表).export(*["packetName"])
            .teardown_hook("${assert_equal($packetName,领劵红包)}")
        ),

    ]


if __name__ == "__main__":
    TestCase新增领劵红包校验().test_start()

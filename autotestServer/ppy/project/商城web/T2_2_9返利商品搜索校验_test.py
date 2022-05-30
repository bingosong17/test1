#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/29 15:09
"""
    概要：
      返利商品列表，选择状态点击搜索
    输入参数：
        "status": "",返利商品状态_status:1:已过期、2:生效、3:未生效不传表示全部
    输出参数：
        msg
    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.营销中心.api.返利商品列表_test import TestCase返利商品列表 as 返利商品列表

class TestCase返利商品搜索校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "status": "2",
        })

    teststeps = [
        Step(
            RunTestCase("返利商品列表").with_variables(**{"status": "2"})
            .call(返利商品列表).export(*["pageData"])
            .teardown_hook("${assert_contains($pageData,生效中)}")
        ),
        Step(
            RunTestCase("返利商品列表").with_variables(**{"status": "1"})
            .call(返利商品列表).export(*["pageData"])
            .teardown_hook("${assert_contains($pageData,已过期)}")
        ),
    ]


if __name__ == "__main__":
    TestCase返利商品搜索校验().test_start()

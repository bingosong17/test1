#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/28 14:30
"""
    概要：
      新人礼包启用停用，查看列表数据校验
    输入参数：
          "operateType": -1表示停用
    输出参数：
        msg
    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.营销中心.api.新人礼包列表_test import TestCase新人礼包列表 as 新人礼包列表
from yyht.营销中心.api.启用停用新人礼包_test import TestCase启用停用新人礼包 as 启用停用新人礼包

class TestCase新人礼包启用停用校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "operateType": -1
        })

    teststeps = [
        Step(
            RunTestCase("新人礼包列表").call(新人礼包列表).export(*["bagId", "status"])
            .teardown_hook("${assert_equal($status,0)}")
        ),
        Step(
            RunTestCase("启用停用新人礼包").call(启用停用新人礼包)
        ),
        Step(
            RunTestCase("新人礼包列表").call(新人礼包列表).export(*["status"])
            .teardown_hook("${assert_equal($status,1)}")
        ),
        Step(
            RunTestCase("启用停用新人礼包").with_variables(
                **
                {"operateType": 1}
            )
            .call(启用停用新人礼包)
        ),
    ]


if __name__ == "__main__":
    TestCase新人礼包启用停用校验().test_start()

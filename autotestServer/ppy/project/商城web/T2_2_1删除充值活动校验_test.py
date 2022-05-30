#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/29 10:52
"""
    概要：
        新增充值活动，充值活动列表做B环验证.再删除该条充值记录
    输入参数：
        "giveAmount": 赠送金额
        "rechargeAmount": 充值金额
    输出参数：

    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.营销中心.api.新增充值活动_test import TestCase新增充值活动 as 新增充值活动
from yyht.营销中心.api.充值活动列表_test import TestCase充值活动列表 as 充值活动列表
from yyht.营销中心.api.删除充值活动_test import TestCase删除充值活动 as 删除充值活动
import env


class TestCase充值活动校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "giveAmount": 0.01,
            "rechargeAmount": 0.01
        })

    teststeps = [
        Step(
            RunTestCase("新增充值活动").call(新增充值活动)
        ),
        Step(
            RunTestCase("充值活动列表").with_variables(
            ).call(充值活动列表).export(*["rechargeAmount", "rechargeId"])
        ),
        Step(
            RunTestCase("删除充值活动").with_variables(
                **{"ruleId": "$rechargeId"})
            .call(删除充值活动)
        ),
        Step(
            RunTestCase("充值活动列表").call(充值活动列表).export(*["rechargeAmount", "rechargeId"])
            .teardown_hook("${assert_not_equal($rechargeAmount,0.01)}")
        ),
    ]


if __name__ == "__main__":
    TestCase充值活动校验().test_start()

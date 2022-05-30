#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/29 15:36
"""
    概要：
      返利商品列表，停用校验
    输入参数：
        "status": "",返利商品状态_status:1:已过期、2:生效、3:未生效不传表示全部
        "switchType": -1, -1表示停用，1启用
    输出参数：
        msg
    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.营销中心.api.返利商品列表_test import TestCase返利商品列表 as 返利商品列表
from yyht.营销中心.api.停用返利商品_test import TestCase停用返利商品 as 停用返利商品

class TestCase返利商品停用校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "statusTo228": "",
            "switchType": -1,
        })

    teststeps = [
        Step(
            RunTestCase("返利商品列表").with_variables(
                **{
                    "status": "$statusTo228",
                }
            ).call(返利商品列表).export(*["pageData"])
        ),
        Step(
            RunTestCase("停用返利商品").with_variables(**{"rebateId":
            "${exportValue($pageData,rebateId,goodsId=5645)}"})
            .call(停用返利商品)
        ),
        Step(
            RunTestCase("返利商品列表").call(返利商品列表)
            .teardown_hook("${assert_contains($pageData,disabledStatus=已停用)}")
        ),
    ]


if __name__ == "__main__":
    TestCase返利商品停用校验().test_start()

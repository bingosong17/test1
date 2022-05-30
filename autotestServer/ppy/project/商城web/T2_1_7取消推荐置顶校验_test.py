# -*- coding: utf-8 -*-
# @Time : 2020/9/17 20:56
# @Author : 郑和
# @File : 推荐置顶校验.py
"""
    概要：
        取消推荐置顶校验
    输入参数：
        无
    输出参数：
        id
    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.商品中心.api.取消推荐_test import TestCase取消推荐 as 取消推荐
from yyht.商品中心.api.在售商品查询_test import TestCase在售商品查询 as 在售商品查询

import env


class TestCase取消推荐置顶校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
        })

    teststeps = [
        Step(
            RunTestCase("取消推荐").with_variables(
                **{
                    "sortId": "1062",
                }
            ).call(取消推荐)
        ),
        Step(
            RunTestCase("在售商品查询").call(在售商品查询).export(*['id'])
            .teardown_hook("${assert_not_equal($id,1062)}")
        ),
    ]


if __name__ == "__main__":
    TestCase取消推荐置顶校验().test_start()

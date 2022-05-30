# -*- coding: utf-8 -*-
# @Time : 2020/9/17 20:56 
# @Author : 郑和
# @File : 推荐置顶校验.py
"""
    概要：
        为商户钱包充钱
    输入参数：
        "phone": 运营后台登陆账号,
        "pass": 运营后台登陆密码
        "cityCode": 运营后台登陆选择城市

        "tradeAmount": 充值数额
        "userphone": 被充值的账号
    输出参数：
        无
    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.商品中心.api.推荐置顶_test import TestCase推荐置顶 as 推荐置顶
from yyht.商品中心.api.在售商品查询_test import TestCase在售商品查询 as 在售商品查询
import env


class TestCase推荐置顶校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
        })

    teststeps = [
        Step(
            RunTestCase("推荐置顶").call(推荐置顶)
        ),
        Step(
            RunTestCase("在售商品查询").call(在售商品查询)
        ),
    ]


if __name__ == "__main__":
    TestCase推荐置顶校验().test_start()

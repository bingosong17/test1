#! /usr/bin/env python
#-*- coding:utf-8 -*-

#author:bingo
"""
    概要：
        为订单派单，且使订单生效（只对订单中有一种商品生效，且供应商列表中第一个供应商可以满足供货，其他情况暂时未考虑）
    输入参数：
        "phone": 运营后台登陆账号
        "pass": 运营后台登陆密码
        "cityCode": 城市编号
        "orderNo": 订单号
    输出参数：
        无
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.订单中心.业务脚本.派单fast_test import TestCase派单 as 订单派单且生效
import env


class TestCase订单派单生效(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "orderNo": "2020111017134010615490",
        })

    teststeps = [
        Step(
            RunTestCase("订单派单且生效").call(订单派单且生效)
        ),
    ]


if __name__ == "__main__":
    TestCase订单派单生效().test_start()


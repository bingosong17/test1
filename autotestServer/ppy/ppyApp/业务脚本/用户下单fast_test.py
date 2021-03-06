#! /usr/bin/env python
#-*- coding:utf-8 -*-

#author:bingo
# NOTE: Generated By HttpRunner v3.1.3
"""
    概要：
        用户对指定商品下单，使用账户余额付款
    输入参数：
        "phone": 登陆手机号
        "goodsId": 商品id
        "goodsNu": 下单商品数量
    输出参数：
        无
    前置接口：
        验证码登陆
"""

from httprunner import HttpRunner, Config, Step, RunTestCase
from ppyApp.api.获取商品明细_test import TestCase获取商品明细 as 获取商品明细
from ppyApp.api.添加商品_test import TestCase添加商品 as 添加商品
from ppyApp.api.创建订单_test import TestCase创建订单 as 创建订单
from ppyApp.api.发起支付_test import TestCase发起支付 as 发起支付
from ppyApp.api.获取订单详情_test import TestCase获取订单详情 as 获取订单详情


class TestCase用户下单(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "ppyApp",
            "phone": "13216168485",
            "token": "${getSession($business,$phone)}",
            "goodsId": "13887",
            "goodsNu": 10
        }
    ).export(*["orderNo"])

    teststeps = [
        Step(
            RunTestCase("获取商品明细").call(获取商品明细)
        ),
        Step(
            RunTestCase("添加商品到购物车").call(添加商品)
        ),
        Step(
            RunTestCase("创建订单").call(创建订单).export(*["orderNo"])
        ),
        Step(
            RunTestCase("发起支付").call(发起支付)
                .teardown_hook("${sleep_N_secs(2)}")
        ),
    ]


if __name__ == "__main__":
    TestCase用户下单().test_start()


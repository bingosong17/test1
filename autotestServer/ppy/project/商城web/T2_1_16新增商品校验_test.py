#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/24 11:30
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.商品中心.api.新增商品_test import TestCase新增商品 as 新增商品
from yyht.商品中心.api.商品列表_test import TestCase商品列表 as 商品列表
import random


class TestCase新增商品校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
             "business": "yyht",
            "session": "${getSession($business)}",
            "name": "可口可乐就这么地1ml/箱",
            "barImageUrl": "",
            "barCode": random.randint(111111111111, 999999999999),
            "barStatus": 1,
            "recycled": 0,
            "specialty": "0",
            "isImport": "0",
            "single": 1,
            "goodsPacknumUnit": "",
            "goodsInsidePackUnit": "",
            "goodsInsidePackNum": None,
            "goodsPacknum": None,
            "goodsCapacity": 1,
            "theoryVolume": 1,
            "weight": 1,
            "scatteredPrice": 1,
            "retailPrice": 1,
            "guaranteePeriod": 1,
            "brand": 4,
            "brandId": 4,
            "specificationDesc": "商品用于测试",
            "manufacturer": "1",
            "backstageCategoryId": 377,
            "logisticsPurchaseNum": 1,
            "storageMethod": "1",

        })

    teststeps = [
        Step(
            RunTestCase("新增商品").call(新增商品)
        ),
        Step(
            RunTestCase("商品列表")
            .call(商品列表).export(*["pageData"])
            .teardown_hook("${assert_contains($pageData,barCode=$barCode}")
        ),
    ]



if __name__ == "__main__":
    TestCase新增商品校验().test_start()


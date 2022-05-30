#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/20 11:18
"""
    概要：
        前台类目排序的校验
    输入参数：
         "receptionCategoryName":前台类目名称
         前台类目的id	---receptionCategoryId
valid---	禁用、启用标志[1：启用;0：禁用]
    输出参数：
       "receptionCategoryId": 前台类目ID
    前置接口：
        无
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.商品中心.api.前台类目展示列表_test import TestCase前台类目展示列表 as 前台类目展示列表
from yyht.商品中心.api.移动排序对象到指定位置_test import TestCase移动排序对象到指定位置 as 移动排序对象到指定位置

import random


class TestCase前台类目排序校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "display": 1,
            "traId": 11,
            "point": 1,

        })

    teststeps = [
        Step(
            RunTestCase("前台类目展示列表").call(前台类目展示列表)
            .export(*["receptionCategoryName", "receptionCategoryId"])

        ),
        Step(
            RunTestCase("移动排序对象到指定位置").with_variables(
                **{
                    "sortId": "$receptionCategoryId"
                }
            )
            .call(移动排序对象到指定位置)
                   ),
        Step(
            RunTestCase("前台类目展示列表").with_variables(
            ).call(前台类目展示列表).export(*["Name"])
            .teardown_hook("${assert_equal($Name,$Name)}")
        ),

    ]


if __name__ == "__main__":
    TestCase前台类目排序校验().test_start()


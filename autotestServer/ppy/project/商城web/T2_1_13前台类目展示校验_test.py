#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/20 10:29
"""
    概要：
        前台类目展示，查看前台类目展示列表，校验数据是否展示
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
from yyht.商品中心.api.新增前台类目_test import TestCase新增前台类目 as 新增前台类目
from yyht.商品中心.api.前台类目展示列表_test import TestCase前台类目展示列表 as 前台类目展示列表
from yyht.商品中心.api.商圈是否显示前台类目_test import TestCase商圈是否显示前台类目 as 商圈是否显示前台类目


class TestCase前台类目展示校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "display": 1,
            "traId": 11,
            "receptionCategoryNameTo2113": "${timeStr(商务)}"

        })

    teststeps = [
        Step(
            RunTestCase("新增前台类目").with_variables(
                **{
                    "receptionCategoryName": "$receptionCategoryNameTo2113"
                }
            ).call(新增前台类目)
        ),
        Step(
            RunTestCase("前台类目展示列表").call(前台类目展示列表)
            .export(*["pageData"])
        ),
        Step(
            RunTestCase("商圈是否显示前台类目").with_variables(**{
                "receptionCategoryId":
                "${exportValue($pageData, receptionCategoryId,"
                "receptionCategoryName=$receptionCategoryNameTo2113)}"})
            .call(商圈是否显示前台类目)
                   ),
        Step(
            RunTestCase("前台类目展示列表").call(前台类目展示列表)
            .teardown_hook("${assert_contains($pageData,display,1)}")
        ),

    ]


if __name__ == "__main__":
    TestCase前台类目展示校验().test_start()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/19 17:09
"""
    概要：
        新增前台类目（一级）再停用该类目，判断字段是否是停用
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
from yyht.商品中心.api.前台一级类目列表_test import TestCase前台一级类目列表 as 前台一级类目列表
from yyht.商品中心.api.启用禁用前台类目_test import TestCase启用禁用前台类目 as 启用禁用前台类目
import random


class TestCase前台类目停用校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "receptionCategoryNameTo2112": "${timeStr(商务物流)}",
            "valid": 0
        })

    teststeps = [
        Step(
            RunTestCase("新增前台类目").with_variables(
                **{
                    "receptionCategoryName": "$receptionCategoryNameTo2112"
                }
            ).call(新增前台类目)
        ),
        Step(
            RunTestCase("前台一级类目列表").call(前台一级类目列表)
            .export(*["pageData"])
        ),
        Step(
            RunTestCase("启用禁用前台类目").with_variables(
                **{
                    "receptionCategoryId":
                    "${exportValue($pageData,receptionCategoryId,"
                    "receptionCategoryName=$receptionCategoryNameTo2112)}",
                    "valid": 0
                }
            ).call(启用禁用前台类目)
        ),
        Step(
            RunTestCase("前台一级类目列表").with_variables(
            ).call(前台一级类目列表).export(*["valid"])
            .teardown_hook("${assert_equal($valid,0)}")
        ),
    ]


if __name__ == "__main__":
    TestCase前台类目停用校验().test_start()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/19 10:06
"""
    概要：
        新增前台类目（一级）判断列表是否新增成功，再删除该前台类目，判断列表是否还有改类目，没有表示删除成功
    输入参数：
         "receptionCategoryName":前台类目名称
    输出参数：
       "receptionCategoryId": 前台类目ID
    前置接口：
        无
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.商品中心.api.新增前台类目_test import TestCase新增前台类目 as 新增前台类目
from yyht.商品中心.api.前台一级类目列表_test import TestCase前台一级类目列表 as 前台一级类目列表
from yyht.商品中心.api.删除前台类目_test import TestCase删除前台类目 as 删除前台类目
import random


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.商品中心.api.新增前台类目_test import TestCase新增前台类目 as 新增前台类目
from yyht.商品中心.api.前台一级类目列表_test import TestCase前台一级类目列表 as 前台一级类目列表
from yyht.商品中心.api.删除前台类目_test import TestCase删除前台类目 as 删除前台类目
import random


class TestCase删除前台类目校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "NameTo2111": "${timeStr(商务物)}"
        })

    teststeps = [
        Step(
            RunTestCase("新增前台类目").with_variables(
                **{
                   "receptionCategoryName": "$NameTo2111"
                }
            ).call(新增前台类目)
        ),
        Step(
            RunTestCase("前台一级类目列表").call(前台一级类目列表).export(*["pageData"])
        ),
        Step(
            RunTestCase("删除前台类目").with_variables(
                **{
                    "receptionCategoryId": "${exportValue($pageData,receptionCategoryId, receptionCategoryName=$NameTo2111)}"
                })
            .call(删除前台类目)
        ),
        Step(
            RunTestCase("前台一级类目列表").call(前台一级类目列表)
         .teardown_hook("${assert_not_contains($pageData,$NameTo2111)}")
        ),
            ]


if __name__ == "__main__":
    TestCase删除前台类目校验().test_start()

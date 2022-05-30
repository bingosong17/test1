# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：承运商名称搜索，查看搜索结果
        环境test
        
    输入参数：
        name    承运商名称
    输出参数：
       name    承运商名称
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.物流中心.运力管理.api.承运商列表查询_test import TestCase承运商列表查询 as 承运商列表
import env


class TestCase承运商名称搜索(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "name": "杭州奥图物流有限公司",

        }
    )

    teststeps = [
        Step(
            RunTestCase("承运商列表").with_variables(
                **{
                    "name": "杭州奥图物流有限公司",
                }

            ).call(承运商列表)
                .teardown_hook("${assert_equal($name,杭州奥图物流有限公司)}")
        ),




    ]

if __name__ == "__main__":
    TestCase承运商名称搜索().test_start()

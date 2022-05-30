# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：按名称搜索标签
        环境test
        
    输入参数：
       name 标签名称
    输出参数：
       name 标签名称
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.数据中心.api.标签列表_test import TestCase标签列表 as 标签列表


class TestCase按名称搜索标签(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",

        }
    )

    teststeps = [
        Step(
            RunTestCase("按标签名搜索标签").with_variables(
                **{
                    "name": "上门收款",
                }

            ).call(标签列表)
                .teardown_hook("${assert_equal($name,'上门收款')}")
        ),



    ]

if __name__ == "__main__":
    TestCase按名称搜索标签().test_start()

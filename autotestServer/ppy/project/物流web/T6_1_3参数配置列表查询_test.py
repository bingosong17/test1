# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：参数配置列表查询
        环境test
        
    输入参数：
        无  
    输出参数：
        cityCode  
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.物流中心.CTMS设置.api.参数配置列表查看_test import TestCase参数配置列表查看 as 参数配置列表查看


class TestCase参数配置列表查看(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
        }
    )

    teststeps = [
        Step(
            RunTestCase("参数配置列表查看").with_variables(
                **{

                }

            ).call(参数配置列表查看)
                .teardown_hook("${assert_equal($cityCode,'330100')}")

        ),

    ]

if __name__ == "__main__":
    TestCase参数配置列表查看().test_start()

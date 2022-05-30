# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：查看司机运力统计，返回统计结果
        环境test
        
    输入参数：
        
    输出参数：
        checkVehTypeName    车型名称
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.物流中心.运力管理.api.运力统计_test import TestCase运力统计 as 运力统计
import env


class TestCase查看用例统计(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "date": "${hapentime(0,1)}",

        }
    )

    teststeps = [
        Step(
            RunTestCase("运力统计").with_variables(
                **{

                }

            ).call(运力统计).export(*['checkVehTypeName'])

                .teardown_hook("${assert_not_equal($checkVehTypeName,'')}")
        ),



    ]

if __name__ == "__main__":
    TestCase查看用例统计().test_start()

# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：运单管理页，按运单编号查询
        环境test  
    输入参数：
        transportationNo  运单编号
    输出参数：
        transportationNo  运单编号
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.物流中心.运力管理.api.查询运费管理_test import TestCase查询运费管理 as 运费查询


class TestCase运费管理列表查询(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "No": "2010091190255931143781146",
        }
    )

    teststeps = [
        Step(
            RunTestCase("按运单编号查询运费").with_variables(
                **{
                    "transportationNo": "$No",
                }

            ).call(运费查询)
                .teardown_hook("${assert_equal($transportationNo,$No)}")

        ),

    ]

if __name__ == "__main__":
    TestCase运费管理列表查询().test_start()

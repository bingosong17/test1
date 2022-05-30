# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：承运商司机管理名称搜索,查看搜索结果
        环境test
        
    输入参数：
       driverName   司机名称
    输出参数：
        name    司机名称
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.物流中心.运力管理.api.承运商司机管理列表_test import TestCase承运商司机管理列表 as 承运商司机管理
import env


class TestCase承运商司机管理名称搜索(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "driverName": "绿雀-左可培",
        }
    )

    teststeps = [
        Step(
            RunTestCase("承运商司机管理").with_variables(
                **{
                    "driverName": "绿雀-罗帅",
                    "status": "",
                    "carrierId": "28",
                    "vehicleType": "",
                }

            ).call(承运商司机管理)
                .teardown_hook("${assert_equal($name,绿雀-罗帅)}")

        ),





    ]

if __name__ == "__main__":
    TestCase承运商司机管理名称搜索().test_start()

# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：司机钱包列表，按司机id搜索司机
        环境test
        
    输入参数：
        driverId  ： 司机id
    输出参数：
        printStatus : 打印状态
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.财务中心.物流结算.api.司机钱包列表_test import TestCase司机钱包列表 as 司机钱包列表


class TestCase司机id查询司机(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",

        }
    )

    teststeps = [
        Step(
            RunTestCase("查看司机钱包列表").with_variables(
                **{

                }

            ).call(司机钱包列表).export(*["id"])
        ),
        Step(
            RunTestCase("按司机id查询司机钱包").with_variables(
                **{
                    "driverId": "$id",
                    "tradeCode": []
                }

            ).call(司机钱包列表)
                .teardown_hook("${assert_equal($driverId,$id)}")
        ),



    ]

if __name__ == "__main__":
    TestCase司机id查询司机().test_start()

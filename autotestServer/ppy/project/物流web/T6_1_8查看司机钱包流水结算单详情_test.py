# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：司机钱包列表，查看司机钱包流水
        环境test
        
    输入参数：
        driverId     司机id
        "tradeCode": ["01"]    流水类型 01 结算单 
    输出参数：
        settlementCode  结算状态
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.财务中心.物流结算.api.司机钱包列表_test import TestCase司机钱包列表 as 司机钱包列表
from yyht.财务中心.物流结算.api.司机钱包流水列表_test import TestCase司机钱包流水列表 as 司机钱包流水列表
from yyht.财务中心.物流结算.api.司机钱包流水结算单详情_test import TestCase司机钱包流水结算单详情 as 司机钱包流水结算单详情


class TestCase司机钱包流水结算单详情(HttpRunner):
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
            RunTestCase("查看司机钱包列表").with_variables(
                **{
                    "driverId": "$id",
                    "cityCode": "330100"
                }

            ).call(司机钱包列表).export(*["id"])
        ),
        Step(
            RunTestCase("查看司机钱包流水").with_variables(
                **{
                    "driverId": "$id",
                    "tradeCode": []
                }

            ).call(司机钱包流水列表).export(*["driverIds", "tradeNo"])
                .teardown_hook("${assert_equal($driverId,$driverIds)}")
        ),




    ]

if __name__ == "__main__":
    TestCase司机钱包流水结算单详情().test_start()

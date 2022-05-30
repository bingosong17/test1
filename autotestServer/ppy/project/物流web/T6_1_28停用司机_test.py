# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：修改司机状态为停用，检查司机状态
        环境test
        
    输入参数：
        "id": "2764",
        "accountStatus": 10
    输出参数：
        "accountStatus": 10
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.物流中心.运力管理.api.编辑司机信息_test import TestCase编辑司机信息 as 编辑司机信息
from yyht.物流中心.运力管理.api.查看司机详情_test import TestCase查看司机详情 as 查看司机详情
from yyht.物流中心.运力管理.api.查询司机列表_test import TestCase查询司机列表 as 司机id
import env


class TestCase编辑司机信息(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",

        }
    )

    teststeps = [
        Step(
            RunTestCase("司机id").with_variables(
                **{
                    "name": "",
                    "accountStatus": "",
                    "phoneNumber": "15831628354",
                }

            ).call(司机id).export(*["driverId"])
        ),
        Step(
            RunTestCase("编辑司机信息").with_variables(
                **{
                    "id": "$driverId",
                    "accountStatus": 10
                }

            ).call(编辑司机信息)
        ),
        Step(
            RunTestCase("查看司机详情").with_variables(
                **{
                    "driverId": "$driverId",
                }
            ).call(查看司机详情)
                .teardown_hook("${assert_equal($accountStatus,10)}")


        ),
        Step(
            RunTestCase("停用司机").with_variables(
                **{
                    "id": "$driverId",
                    "accountStatus": 50
                }

            ).call(编辑司机信息)
        ),



    ]

if __name__ == "__main__":
    TestCase编辑司机信息().test_start()

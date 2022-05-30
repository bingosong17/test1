# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：修改承运商司机合作状态为合作中（50），在合作中列表可以查到这个司机
        环境test
        
    输入参数：
       cooperationStatus    合作状态
    输出参数：
       driverName   司机名称
    前置接口：
        承运商司机管理
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.物流中心.运力管理.api.承运商司机管理列表_test import TestCase承运商司机管理列表 as 承运商司机管理
from yyht.物流中心.运力管理.api.承运商司机修改合作状态_test import  TestCase承运商司机修改合作状态 as 修改司机状态
import env


class TestCase承运商名称搜索(HttpRunner):
    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "id":"",
            "driverName":""
        }
    )

    teststeps = [
        Step(
            RunTestCase("承运商司机管理").with_variables(
                **{
                    "driverName": "",
                    "status": "",
                    "carrierId": "28",
                    "vehicleType": "",
                }

            ).call(承运商司机管理).export(*["id","name"])

        ),
        Step(
            RunTestCase("修改司机状态").with_variables(
                **{
                    "id": "$id",
                    "cooperationStatus": "50"
                }

            ).call(修改司机状态)

        ),
        Step(
            RunTestCase("承运商司机管理").with_variables(
                **{
                    "driverName": "$name",
                    "status": "50",
                    "carrierId": "28",
                    "vehicleType": "",

                }

            ).call(承运商司机管理)
                .teardown_hook("${assert_equal($driverName,$name)}")

        ),



    ]

if __name__ == "__main__":
    TestCase承运商名称搜索().test_start()

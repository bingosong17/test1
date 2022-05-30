# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：删除车队，检查结果删除成功
        环境test
        
    输入参数：
       fleetName    车队名称
    输出参数：
    
    前置接口：
        TestCase新建车队
        TestCase车队管理列表查询
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.物流中心.运力管理.api.车队管理列表查询_test import TestCase车队管理列表查询 as 车队管理列表查询
from yyht.物流中心.运力管理.api.新建车队_test import TestCase新建车队 as 新建车队
from yyht.物流中心.运力管理.api.删除车队_test import TestCase删除车队 as 删除车队
import env


class TestCase删除车队(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "fleetNames":  "${createRandomNumber(7)}"
        }
    )

    teststeps = [

        Step(
            RunTestCase("新建车队").with_variables(
                **{
                    "fleetName": "$fleetNames",
                }

            ).call(新建车队).teardown_hook("${sleep_N_secs(3)}")

        ),


        Step(
            RunTestCase("查询车队").with_variables(
                **{
                    "fleetName": "$fleetNames",
                    "driverName": "",
                }

            ).call(车队管理列表查询).teardown_hook("${sleep_N_secs(3)}")
                # .teardown_hook("${assert_equal($fleetName,$fleetNames)}")

        ),
        Step(
            RunTestCase("删除车队").with_variables(
                **{
                    "fleetId": "$fleetId",
                }
            ).call(删除车队)
            .teardown_hook("${assert_equal($body,True)}")

        ),
    ]


if __name__ == "__main__":
    TestCase删除车队().test_start()

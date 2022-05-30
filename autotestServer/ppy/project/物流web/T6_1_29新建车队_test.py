# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：新建车队，列表检查
        环境test
        
    输入参数：
        fleetNames  车队名称
    输出参数：
        fleetNames  车队名称
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.物流中心.运力管理.api.车队管理列表查询_test import TestCase车队管理列表查询 as 车队管理列表查询
from yyht.物流中心.运力管理.api.新建车队_test import TestCase新建车队 as 新建车队
import env


class TestCase按车队名称搜索车队(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "fleetNames":  "${createRandomString(7)}"
        }
    )

    teststeps = [

        Step(
            RunTestCase("新建车队").with_variables(
                **{
                    "fleetName": "$fleetNames",
                }

            ).call(新建车队)

        ),
        Step(
            RunTestCase("查询车队").with_variables(
                **{
                    "fleetName": "$fleetNames",
                    "driverName": "",
                }

            ).call(车队管理列表查询)
                .teardown_hook("${assert_equal($fleetName,$fleetNames)}")

        ),





    ]

if __name__ == "__main__":
    TestCase按车队名称搜索车队().test_start()

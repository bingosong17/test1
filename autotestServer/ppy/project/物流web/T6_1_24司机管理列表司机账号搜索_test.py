# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：在司机管理列表输入司机账号，搜索司机，搜索结果存在当前司机
        环境test
        
    输入参数：
        "phoneNumber": "15267049232"
    输出参数：
        "phoneNumber": "15267049232"
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.物流中心.运力管理.api.查询司机列表_test import TestCase查询司机列表 as 司机账号搜索
import env


class TestCase司机管理列表司机账号搜索(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",

        }
    )

    teststeps = [
        Step(
            RunTestCase("按司机名称搜索").with_variables(
                **{
                    "phoneNumber": "15267049232",
                }
            ).call(司机账号搜索).export(*["phoneNumber"])
                .teardown_hook("${assert_equal($phoneNumber,'15267049232')}")
        ),


    ]


if __name__ == "__main__":
    TestCase司机管理列表司机账号搜索().test_start()

# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：新增司机，并在列表中搜索司机
        环境test
        
    输入参数：
        "phoneNumber":手机号
    输出参数：
        "phoneNumber": 手机号
    前置接口：
        TestCase新增司机
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.物流中心.运力管理.api.查询司机列表_test import TestCase查询司机列表 as 司机账号搜索
from yyht.物流中心.运力管理.api.新增司机_test import TestCase新增司机 as 新增司机


class TestCase新增员工司机(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "createPhoneNumber": "120${createRandomNumber(8)}"

        }
    )

    teststeps = [
        Step(
            RunTestCase("TestCase新增司机").with_variables(
                **{
                    "phoneNumber": "$createPhoneNumber"
                }
            ).call(新增司机).export(*["phoneNumber"])
        ),
        Step(
            RunTestCase("按司机账号").with_variables(
                **{
                    "phoneNumber": "$createPhoneNumber",
                    "name": "",
                    "accountStatus": "",
                }
            ).call(司机账号搜索).export(*["phoneNumber"])
                .teardown_hook("${sleep(3)}")
                .teardown_hook("${assert_equal($phoneNumber,$createPhoneNumber)}")
        ),


    ]


if __name__ == "__main__":
    TestCase新增员工司机().test_start()
    pass

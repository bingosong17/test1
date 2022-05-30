# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：编辑司机银行账户信息，检查修改后的结果
        环境test
        
    输入参数：
        "id": "2764",  司机id
        bankAccountName 银行账号信息
    输出参数：
        bankAccountName 银行账号信息
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
            "business": "pd",
            "session": "${getSession($business)}",
            "names": "${createRandomString(3)}"
        }
    )

    teststeps = [
        Step(
            RunTestCase("司机id").with_variables(
                **{
                    "name": "",
                    "accountStatus":"" ,
                    "phoneNumber": "15831628354",
                }

            ).call(司机id).export(*["driverId"])
        ),
        Step(
            RunTestCase("编辑司机信息").with_variables(
                **{
                    "id": "$driverId",
                    "name":"$names"
                }

            ).call(编辑司机信息).teardown_hook("${sleep_N_secs(3)}")
        ),
        Step(
            RunTestCase("查看司机详情").with_variables(
                **{
                    "driverId": "$driverId",
                }
            ).call(查看司机详情).export(*["name"])

                .teardown_hook("${assert_equal($name,$names)}")


        ),



    ]

if __name__ == "__main__":
    TestCase编辑司机信息().test_start()

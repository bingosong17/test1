# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：送货单打印页司机搜索
        环境test  
    输入参数：
        driverNameOrPhone 司机名称或手机号
    输出参数：
        name 司机名称
        phoneNumber 司机手机号
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from wlApp.api.送货单打印页搜索司机_test import TestCase送货单打印页搜索司机 as 送货单打印页搜索司机


class TestCase送货单打印页司机搜索(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "business": "wlApp",
            "driverPhone": "15997336112",
            "token": "${getSession($business,$driverPhone)}",
            "userId": "${getWlAppUserId($driverPhone)}",
            "dirverPhoneToSearch": "15997336112"
            # "driverNameOrPhone": "杨杨"  # 15997336112

        }
    )

    teststeps = [
        Step(
            RunTestCase("按司机名称搜索").with_variables(
                **{
                    "driverNameOrPhone": "杨杨",
                    "phoneNumber": "",
                }

            ).call(送货单打印页搜索司机).export(*["name"])
                .teardown_hook("${assert_equal($name,$driverNameOrPhone)}")

        ),
        Step(
            RunTestCase("按司机名账号").with_variables(
                **{
                    "driverNameOrPhone": "$dirverPhoneToSearch"  # 15997336112
                }

            ).call(送货单打印页搜索司机).export(*["phoneNumber"])
                .teardown_hook("${assert_equal($phoneNumber,'$dirverPhoneToSearch')}")

        ),
    ]

if __name__ == "__main__":
    TestCase送货单打印页司机搜索().test_start()

# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：查送货单打印详情
        环境test
        
    输入参数：
        id  ： 运单id
    输出参数：
        printStatus : 打印状态
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.物流中心.CTMS设置.api.送货单打印列表_test import TestCase送货单打印列表 as 送货单打印列表
from yyht.物流中心.CTMS设置.api.送货单打印详情_test import TestCase送货单打印详情 as 送货单打印详情


class TestCase送货单打印详情(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",

        }
    )

    teststeps = [
        Step(
            RunTestCase("待打印的运单").with_variables(
                **{
                    "printStatus":1
                }

            ).call(送货单打印列表).export(*["printStatus", "id", "driverName"])
        ),
        Step(
            RunTestCase("送货单打印详情").with_variables(
                **{
                    "transOrderId": "$id"
                }

            ).call(送货单打印详情)
                .teardown_hook("${assert_equal($printStatus,1)}")
        ),



    ]

if __name__ == "__main__":
    TestCase送货单打印详情().test_start()

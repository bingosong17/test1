# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：查看车型计价表信息
        环境test
    输入参数：
        driverType  司机类型  
    输出参数：
        freightRulesId  运费规则id
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.物流中心.CTMS设置.api.众包司机取送计价列表查询_test import TestCase众包司机取送计价列表查询 as 众包司机取送计价列表查询
from yyht.物流中心.CTMS设置.api.获取计价表信息_test import TestCase获取计价表信息 as 获取计价表信息


class TestCase获取计价表信息(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",

        }
    )

    teststeps = [
        Step(
            RunTestCase("参数配置列表查看").with_variables(
                **{
                    "driverType": "1"
                }

            ).call(众包司机取送计价列表查询)
                .teardown_hook("${assert_equal($driverType,1)}")

        ),
        Step(
            RunTestCase("TestCase获取计价表信息").with_variables(
                **{
                    "freightRulesId": "$id"
                }

            ).call(获取计价表信息).export(*["id"])
            .teardown_hook("${assert_equal($id,$freightRulesId)}")

        ),
    ]


if __name__ == "__main__":
    TestCase获取计价表信息().test_start()

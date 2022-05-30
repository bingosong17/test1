# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：增加商品配置
        环境test
        
    输入参数：
        goodsName 商品名称 
    输出参数：
        goodsName 商品名称  
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunTestCase,client
from yyht.物流中心.CTMS设置.api.增加商品配置_test import TestCase增加商品配置 as 增加商品配置
from yyht.物流中心.CTMS设置.api.商品配置查询_test import TestCase商品配置查询 as 商品配置查询


class TestCase增加商品配置(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "goodsNames": "${createRandomNumber(5)}"
        }
    )

    teststeps = [
        Step(
            RunTestCase("增加商品配置").with_variables(
                **{
                    "goodsName": "$goodsNames"
                }

            ).call(增加商品配置)

        ),
        Step(
            RunTestCase("商品配置查询").with_variables(
                **{

                }

            ).call(商品配置查询).export(*["goodsName"])
                .teardown_hook("${assert_equal($goodsName,$goodsNames)}")

        ),

    ]

if __name__ == "__main__":
    TestCase增加商品配置().test_start()

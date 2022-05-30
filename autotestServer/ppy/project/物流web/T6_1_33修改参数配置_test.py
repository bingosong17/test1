# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：修改参数配置
        环境test
        
    输入参数：
       transportationNo  运单编号
    输出参数：
        dataDescs 名称
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.物流中心.CTMS设置.api.参数配置列表查看_test import TestCase参数配置列表查看 as 参数配置列表查看
from yyht.物流中心.CTMS设置.api.修改参数设置_test import TestCase修改参数设置 as 修改参数设置


class TestCase修改参数设置(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "dataDescs": "司机使用app间断预警值（单位min）"+"${createRandomString(3)}",
        }
    )

    teststeps = [
        Step(
            RunTestCase("修改参数设置").with_variables(
                **{
                    "dataDesc": "$dataDescs",
                    "id": "560",
                }

            ).call(修改参数设置)

        ),
        Step(
            RunTestCase("参数配置列表查看").with_variables(
                **{

                }

            ).call(参数配置列表查看).export(*["dataDesc"])
                .teardown_hook("${assert_equal('$dataDesc','$dataDescs')}")

        ),

    ]

if __name__ == "__main__":
    TestCase修改参数设置().test_start()

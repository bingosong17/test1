# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：查看司机运力统计，返回统计结果
        环境test
        
    输入参数：
        name    主管名称
    输出参数：
        name    主管名称
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.物流中心.运力管理.api.服务主管列表查询_test import TestCase服务主管列表查询 as 服务主管搜索
from yyht.物流中心.运力管理.api.新增服务主管_test import TestCase新增服务主管 as 新增服务主管



class TestCase搜多服务主管(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "names": "${createRandomString(3)}",
            "phone": "120${createRandomNumber(8)}",

        }
    )

    teststeps = [
        Step(
            RunTestCase("新增服务主管").with_variables(
                **{
                    "name": "$names"
                }

            ).call(新增服务主管)
        ),
        Step(
            RunTestCase("服务主管搜索").with_variables(
                **{
                    "name": "$names"
                }

            ).call(服务主管搜索)
                .teardown_hook("${assert_equal($name,$names)}")
        ),



    ]

if __name__ == "__main__":
    TestCase搜多服务主管().test_start()

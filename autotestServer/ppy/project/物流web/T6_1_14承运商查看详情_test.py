# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：查看承运商详情
        环境test
        
    输入参数：
       id   承运商id
    输出参数：
       carrierId    承运商id
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.物流中心.运力管理.api.承运商列表查询_test import TestCase承运商列表查询 as 承运商列表
from yyht.物流中心.运力管理.api.查看供应商详情_test import TestCase查看供应商详情 as 供应商详情
import env


class TestCase承运商名称搜索(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "id":""
        }
    )

    teststeps = [
        Step(
            RunTestCase("承运商列表").with_variables(
                **{
                    "name": "",
                }

            ).call(承运商列表)

        ),
        Step(
            RunTestCase("供应商详情").with_variables(
                **{
                    "id": "$id"
                }

            ).call(供应商详情)
                .teardown_hook("${assert_equal($id,$carrierId)}")
        ),




    ]

if __name__ == "__main__":
    TestCase承运商名称搜索().test_start()

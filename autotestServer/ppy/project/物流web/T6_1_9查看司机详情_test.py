# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：查看司机详情，返回司机id信息
        环境test
        
    输入参数：
        "driverId": 司机id
    输出参数：
        "driverId": 司机id
    前置接口：
        无
"""
import sys
from pathlib import Path
# sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.物流中心.运力管理.api.查看司机详情_test import TestCase查看司机详情 as 司机详情
from yyht.物流中心.运力管理.api.查询司机列表_test import TestCase查询司机列表 as 司机id
from debugtalk import insertRootPath

insertRootPath()

class TestCase查看司机详情(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
        }
    )

    teststeps = [
        Step(
            RunTestCase("司机id").with_variables(
                **{
                    "name": "",
                    "accountStatus": "",
                    "phoneNumber": "15831628354",
                }

            ).call(司机id).export(*["driverId"])
        ),
        Step(
            RunTestCase("司机详情").with_variables(
                **{
                    "driverId": "$driverId",
                }
            ).call(司机详情).export(*["detailDriverIdStr"])
            .teardown_hook("${assert_equal($driverId,$detailDriverIdStr)}")
        ),



    ]


if __name__ == "__main__":
    TestCase查看司机详情().test_start()

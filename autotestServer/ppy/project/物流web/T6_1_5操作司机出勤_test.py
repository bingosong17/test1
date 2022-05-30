# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：操作司机当天出勤状态为出勤，再检查出勤状态
        环境test
        
    输入参数：
        "type": "0",  出勤状态
        "driverId": "635", 司机id
    输出参数：
        "content"   出勤描述
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.物流中心.运力管理.api.查看司机出勤状态_test import TestCase查看司机出勤状态 as 查看司机出勤状态
from yyht.物流中心.运力管理.api.司机出勤_test import TestCase操作司机出勤 as 操作司机出勤
import env


class TestCase查看司机出勤状态(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",

        }
    )

    teststeps = [
        Step(
            RunTestCase("操作司机出勤").with_variables(
                **{
                    "type": "0",
                    "driverId": "635",
                }
            ).call(操作司机出勤)
        ),
        Step(
            RunTestCase("查看司机出勤状态").with_variables(
                **{
                    "driverId": "635",
                }
            ).call(查看司机出勤状态).export(*["content"])
                .teardown_hook("${assert_equal($content,出勤)}")
        ),


    ]


if __name__ == "__main__":
    TestCase查看司机出勤状态().test_start()

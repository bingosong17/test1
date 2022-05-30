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
        date 出勤日期
    输出参数：
        executeTime 出勤日期
        attendanceType  出勤类型
    前置接口：
        TestCase司机操作出勤
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from wlApp.api.司机操作出勤_test import TestCase司机操作出勤 as 司机操作出勤
from wlApp.api.司机出勤统计_test import TestCase操作司机出勤 as 操作司机出勤



class TestCase操作司机出勤(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "business": "wlApp",
            "driverPhone": "15997336112",
            "token": "${getSession($business,$driverPhone)}", #$phoneNumber
            "userId": "${getWlAppUserId($driverPhone)}",  # $phoneNumber
            "date": "${hapentime(0,3)}",
            "dates": "${hapentime(48,1,h)}",
        }
    )

    teststeps = [
        Step(
            RunTestCase("司机操作出勤").with_variables(
                **{
                    "date": "$dates",
                    "type": 0,
                    "phoneNumber": "$phoneNumber",
                }

            ).call(司机操作出勤)
                # .teardown_hook("${sleep(3)}")
        ),
        Step(
            RunTestCase("检查当天司机出勤状态").with_variables(
                **{
                    "date": "$date",
                }

            ).call(操作司机出勤).export(*["body"])
                # 检查出勤日启和出勤状态同时符合条件
            .teardown_hook("${sleep(1)}")
                .teardown_hook("${assert_contains($body,executeTime=$dates,attendanceType=0)}")


        ),



    ]

if __name__ == "__main__":
    TestCase操作司机出勤().test_start()

#! /usr/bin/env python
#-*- coding:utf-8 -*-

#author:bingo

# NOTE: Generated By HttpRunner v3.1.3
"""
    概要：
        用户创建订单完成付款，后台完成派单，生效操作
    输入参数：
        "phone": 运营后台登陆账号
        "pass": 运营后台登陆密码
        "cityCode": 城市编号
        "orderNo": 订单号
    输出参数：
        "transOrderId":运单编号
        "phoneNumber":司机联系电话
    前置接口：
        无
"""

from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.物流中心.运单管理.api.运单列表_test import TestCase运单列表 as 运单列表


class TestCase通过订单获取运单id(HttpRunner):

    config = Config("testcase description").verify(False).variables(
        **{
            "business": "pd",
            "session": "${getSession($business)}",
            "transOrderId": "",
            "orderNo": None,
            "driverName": None,
            "driverId": None,
            "driverPhoneNumber": None,
            "id": None,
            "startTime": None,
            "endTime": None,
            "pageNum": 1,
            "plannedStartTime": "",
            "plannedEndTime": "",
            "pageSize": 10,
            "transOrderStatus": "",
            "sortRule": "101",
            "type": None,
            "driverTypeList": None,
            "zoneCodeList": None,
        }).export(*["transOrderId", "phoneNumber"])
    teststeps = [
        Step(
            RunTestCase("查看运单列表").call(运单列表).export(*["transOrderId", "phoneNumber"])
        ),
    ]


if __name__ == "__main__":
    TestCase通过订单获取运单id().test_start()

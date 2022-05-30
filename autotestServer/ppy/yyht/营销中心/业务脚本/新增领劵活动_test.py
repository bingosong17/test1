#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/19 14:22
"""
    概要：
        新增领劵活动，先新增领劵红包，再利用该红包创建活动
    输入参数：
        "startTime": "2020-10-19 13:57:22",--开始时间
            "endTime": "2020-11-18 13:55:22",---结束时间
            "traIds": [11],--对应商圈
            "assignType": 1,---指定用户类型 0 指定用户 1指定商圈 2指定标签用户
            "couponName": "领劵活动名称",
            "display": 1,---是否入口展示（0不显示，1显示）
            "labelName": "",---指定标签时传入用户标签名称
            "redPacketId": 240568, --- 红包ID
    输出参数：
        packetId ：红包ID

    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.营销中心.业务脚本.新增领劵红包_test import TestCase新增领劵红包 as 新增领劵红包
from yyht.营销中心.api.创建编辑领劵活动_test import TestCase创建编辑领劵活动 as 创建编辑领劵活动

class TestCase新增领劵活动(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "packetName": "领劵红包7",
            "startTime": "2020-10-19 15:25:22",
            "endTime": "2020-11-18 13:55:22",
            "traIds": [11],
            "assignType": 1,
            "couponName": "领劵活动7",
            "display": 1,
        })

    teststeps = [
        Step(
            RunTestCase("新增领劵红包").call(新增领劵红包).export(*["packetId"])
            .teardown_hook("${sleep_N_secs(2)}")
        ),
        Step(
            RunTestCase("创建编辑领劵活动").with_variables(
                **{
                    "redPacketId": "$packetId",
                }
            ).call(创建编辑领劵活动)
            .teardown_hook("${sleep_N_secs(2)}")
        ),

    ]


if __name__ == "__main__":
        TestCase新增领劵活动().test_start()

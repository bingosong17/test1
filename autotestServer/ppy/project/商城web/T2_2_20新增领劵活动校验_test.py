#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/19 15:40
"""
    概要：
        新增领劵红活动，对应领劵红包，查看领劵活动列表是否有该数据
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
        $packetName： 会员红包名称
    前置接口：
        用户登陆
"""
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase, client
from yyht.营销中心.业务脚本.新增领劵活动_test import TestCase新增领劵活动 as 新增领劵活动
from yyht.营销中心.api.领劵活动列表_test import TestCase领劵活动列表 as 领劵活动列表
import env


class TestCase新增领劵活动校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "packetName": "领劵红包7",
            "startTime": "${hapentime(1)}"+":00",
            "endTime": "${hapentime(100)}"+":00",
            "traIds": [11],
            "assignType": 1,
            "couponName": "领劵活动7",
            "display": 1,


        })

    teststeps = [
        Step(
            RunTestCase("新增领劵活动").call(新增领劵活动)
        ),
        Step(
            RunTestCase("领劵活动列表").call(领劵活动列表).export(*["couponName"])
            .teardown_hook("${assert_equal($couponName,领劵活动7)}")
        ),

    ]


if __name__ == "__main__":
    TestCase新增领劵活动校验().test_start()

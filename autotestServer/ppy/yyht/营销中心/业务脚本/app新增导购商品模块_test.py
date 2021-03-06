# -*- coding: utf-8 -*-
# @Time : 2020/9/9 15:03 
# @Author : 郑和
# @File : app新增导购商品模块_test.py

# NOTE: Generated By HttpRunner v3.1.3
"""
    概要：
        为商户钱包充钱
    输入参数：
        "phone": 运营后台登陆账号,
        "pass": 运营后台登陆密码
        "cityCode": 运营后台登陆选择城市

        "tradeAmount": 充值数额
        "userphone": 被充值的账号
    输出参数：
        无
    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.用户登陆_test import TestCase用户登陆 as 用户登陆
from yyht.营销中心.api.创建专题信息无活动专题_test import TestCase创建专题信息无活动专题 as 创建专题信息无活动专题
from yyht.营销中心.api.获取专题详情_test import TestCase获取专题详情 as 获取专题详情
from yyht.营销中心.api.导入指定商品id列表_test import TestCase导入指定商品Id列表 as 导入指定商品Id列表
from yyht.营销中心.api.创建导购信息_test import TestCase创建导购信息 as 创建导购信息



class TestCaseapp新增导购商品模块(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "pass": "123456",
            "cityCode": "330100",
            "startTime": "2020-09-11 20:57:44",
            "endTime": "2020-10-07 20:54:44",
            "traIds": [11, 13, 14, 20, 104, 171, 173, 174, 177, 178, 386, 395],
            "guideName": "导购1",


        })

    teststeps = [
        Step(
            RunTestCase("用户登陆").call(用户登陆).export(*["session"])
        ),
        Step(
            RunTestCase("创建专题信息无活动专题").call(创建专题信息无活动专题).export(*["topicId"])
                .teardown_hook("${sleep_N_secs(2)}")
        ),
        Step(
            RunTestCase("获取专题详情").call(获取专题详情).teardown_hook("${sleep_N_secs(2)}")
        ),
        Step(
            RunTestCase("导入指定商品Id列表").call(导入指定商品Id列表).teardown_hook("${sleep_N_secs(2)}")
        ),
        Step(
            RunTestCase("创建导购信息").with_variables(
                **{
                    "actionParam": "$topicId"
                }
            ).call(创建导购信息).teardown_hook("${sleep_N_secs(2)}")
        ),
    ]


if __name__ == "__main__":
    TestCaseapp新增导购商品模块().test_start()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/28 16:59
"""
    概要：
        查看促销中的爆品，将列表中的第一个取消促销，查看取消促销列表中是否新增这条数据
    输入参数：
            "status": " ",状态status_0:未生效、1:促销中、2:已结束、3:已取消
    输出参数：

    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.营销中心.api.新增爆品_test import TestCase新增爆品 as 新增爆品
from yyht.营销中心.api.爆品列表_test import TestCase爆品列表 as 爆品列表
from yyht.营销中心.api.取消促销_test import TestCase取消促销 as 取消促销


class TestCase取消促销校验(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "status": "1",
            "redPacketAvailable": 0,
            "promotionsType": 0,
            "goodsIdToBaoPin": 58,
            "traId": 11,
            "promotionsPrice": 35,
            "maxNum": 4,
            "initStock": 5,
            "startTime": "${hapentime(5,2,s)}",
            "endTime": "${hapentime(100,2)}",
            "operateType": "save",

        })

    teststeps = [
        Step(
            RunTestCase("新增爆品").with_variables(
                **{
                    "goodsId": "$goodsIdToBaoPin"
                }
            ).call(新增爆品)
        ),
        Step(
            RunTestCase("爆品列表").with_variables(**{
                "status": "",
            })
            .call(爆品列表).export(*["pageData"])
            .teardown_hook("${sleep_N_secs(5)}")
        ),
        Step(
            RunTestCase("取消促销")
            .with_variables(
                **{
                   "surpriseId": "${exportValue($pageData,id,goodsId=58)}"}
            )
            .call(取消促销)
            .teardown_hook("${sleep_N_secs(1)}")
        ),
        Step(
            RunTestCase("爆品列表")
            .with_variables(
                **{"status": "3"})
            .call(爆品列表).export(*["pageData"])
            .teardown_hook("${assert_contains($pageData,id=$id)}")

        ),
    ]


if __name__ == "__main__":
    TestCase取消促销校验().test_start()

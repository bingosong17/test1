#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/28 16:50
"""
    概要：
        新增爆品校验，在删除，查看列表数据
    输入参数：
        "redPacketAvailable": 是否使用红包(0-不使用、1-使用
        "promotionsType": 促销类型  0：一般爆品，1：特价爆品
        "goodsId": 商品ID
        "traId": 商圈id
        "promotionsPrice": 促销价
        "maxNum": 限购量
        "initStock":限购库存
        "startTime": 活动开始时间
        "endTime": 活动结束时间
        "operateType": 操作类型不能为空，save-新增、update-更新
    输出参数：
        $backgroundImageName： 背景图名称,
    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.营销中心.api.新增爆品_test import TestCase新增爆品 as 新增爆品
from yyht.营销中心.api.爆品列表_test import TestCase爆品列表 as 爆品列表
from yyht.营销中心.api.删除爆品_test import TestCase删除爆品 as 删除爆品


class TestCase删除爆品校验(HttpRunner):
    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "redPacketAvailable": 0,
            "promotionsType": 0,
            "goodsIdTo222": 351,
            "traId": 11,
            "promotionsPrice": 35,
            "maxNum": 4,
            "initStock": 5,
            "startTime": "${hapentime(1)}" + ":00",
            "endTime": "${hapentime(100)}" + ":00",
            "operateType": "save",
        })

    teststeps = [
        Step(
            RunTestCase("新增爆品").with_variables(
                **{
                    "goodsId": "$goodsIdTo222",
                }
            ).call(新增爆品)
        ),
        Step(
            RunTestCase("爆品列表").with_variables(
                **{
                    "status": "0",
                }
            ).call(爆品列表).export(*["pageData"])
        ),
        Step(
            RunTestCase("删除爆品")
            .with_variables(
                **{"surpriseId": "${exportValue($pageData,id,goodsId=intType$goodsIdTo222)}"}
            )
            .call(删除爆品)
        ),
        Step(
            RunTestCase("爆品列表").with_variables(
                **{
                    "status": "0",
                }
            ).call(爆品列表).export(*["goodsId", "id"])
            .teardown_hook("${assert_not_equal($goodsId,351)}")
        ),
    ]


if __name__ == "__main__":
    TestCase删除爆品校验().test_start()

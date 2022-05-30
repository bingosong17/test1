# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：运营费管理页，作废单据
        环境test
    输入参数：
       description  ：运费名称
    输出参数：
        description  ：运费名称
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.物流中心.运力管理.api.添加运费_test import TestCase添加运费 as 添加运费
from yyht.物流中心.运力管理.api.运营费用列表查询_test import TestCase运营费用列表查询 as 运营费用列表查询
from yyht.物流中心.运力管理.api.作废运营费_test import TestCase作废运营费 as 作废运营费
from yyht.物流中心.运力管理.api.查询司机列表_test import TestCase查询司机列表 as 司机查询


class TestCase运营费提交(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "descriptions": "${createRandomNumber(7)}"
        }
    )

    teststeps = [
        Step(
            RunTestCase("司机查询").with_variables(
                **{
                    "name": "",
                    "pageNum": 1,
                    "pageSize": 9999,
                    "accountStatus": 50,
                    "driverTypeList": [1, 50, 40]
                }

            ).call(司机查询).export(*["driverId"])
        ),
        Step(
            RunTestCase("添加运费").with_variables(
                **{
                    "description": "$descriptions",
                    "driverId": "$driverId"
                }

            ).call(添加运费)

        ),
        Step(
            RunTestCase("运费查询").with_variables(
                **{
                    "id": "",
                }

            ).call(运营费用列表查询).export(*["pageData"])

        ),
        Step(
            RunTestCase("作废运营费").with_variables(
                **{
                    "operateCostDetailId": "${exportValue($pageData,id,description=strType$descriptions)}"
                }

            ).call(作废运营费)

        ),
        Step(
            RunTestCase("运费查询").with_variables(
                **{
                    "id": "${exportValue($pageData,id,description=strType$descriptions)}"
                }

            ).call(运营费用列表查询).export(*["totalSize"])
                .teardown_hook("${assert_equal($totalSize,0)}")
        ),
    ]


if __name__ == "__main__":
    TestCase运营费提交().test_start()

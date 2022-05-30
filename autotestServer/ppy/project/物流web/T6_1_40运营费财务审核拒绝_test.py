# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：运营费管理页，业务审核通过
        环境test
    输入参数：
       description  ：运费名称
    输出参数：
        status  ：状态   40 审核驳回
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.物流中心.运力管理.api.添加运费_test import TestCase添加运费 as 添加运费
from yyht.物流中心.运力管理.api.运营费用列表查询_test import TestCase运营费用列表查询 as 运营费用列表查询
from yyht.物流中心.运力管理.api.提交运营费_test import TestCase提交运营费 as 提交运营费
from yyht.物流中心.运力管理.api.业务审核通过_test import TestCase业务审核通过 as 业务审核通过
from yyht.物流中心.运力管理.api.运营费财务审核驳回_test import TestCase运营费财务审核驳回 as 运营费财务审核驳回
from yyht.物流中心.运力管理.api.查询司机列表_test import TestCase查询司机列表 as 司机查询


class TestCase运营费业务审核通过(HttpRunner):
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
                    "statusList": [],
                }

            ).call(运营费用列表查询).export(*["pageData"]).teardown_hook("${sleep_N_secs(1)}")

        ),
        Step(
            RunTestCase("提交运费").with_variables(
                **{
                    "ids": ["${exportValue($pageData,id,description=strType$descriptions)}"]
                }

            ).call(提交运营费)

        ),
        Step(
            RunTestCase("业务审核通过").with_variables(
                **{
                    "ids":["${exportValue($pageData,id,description=strType$descriptions)}"]
                }

            ).call(业务审核通过).teardown_hook("${sleep_N_secs(1)}")
        ),
        Step(
            RunTestCase("财务审核驳回").with_variables(
                **{
                    "operateCostDetailId": "${exportValue($pageData,id,description=strType$descriptions)}"
                }

            ).call(运营费财务审核驳回).teardown_hook("${sleep_N_secs(1)}")
        ),
        Step(
            RunTestCase("运费查询").with_variables(
                **{
                    "id": "${exportValue($pageData,id,description=strType$descriptions)}",
                    "statusList": [],
                }

            ).call(运营费用列表查询).export(*["status"])
                .teardown_hook("${assert_equal($status,40)}")
        ),
    ]


if __name__ == "__main__":
    TestCase运营费业务审核通过().test_start()

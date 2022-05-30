# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：运营费管理页，编辑运营费
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
from yyht.物流中心.运力管理.api.编辑运营费_test import TestCase编辑运营费 as 编辑运营费
from yyht.物流中心.运力管理.api.运营费用列表查询_test import TestCase运营费用列表查询 as 运营费用列表查询
from yyht.物流中心.运力管理.api.查询司机列表_test import TestCase查询司机列表 as 司机查询

class TestCase编辑运费(HttpRunner):
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

            ).call(运营费用列表查询).export(*["pageData"])
        ),
        Step(
            RunTestCase("编辑运营费").with_variables(
                **{
                    "id": "${exportValue($pageData,id,description=strType新增名称)}",
                    "description": "$descriptions",
                }

            ).call(编辑运营费)

        ),
        Step(
            RunTestCase("运费查询").with_variables(
                **{
                    "id": "",
                    "statusList": [],
                }

            ).call(运营费用列表查询).export(*["pageData"])
                # .teardown_hook("${assert_equal($description,$descriptions)}")
                .teardown_hook("${assert_contains($pageData,description=$descriptions)}")
        ),
    ]


if __name__ == "__main__":
    TestCase编辑运费().test_start()

# -*- coding: utf-8 -*-
'''
@Created on 2020/9/17 
@Author  : LiHao
'''

"""
    概要：
        测试点：启用停用标签
        环境test
        
    输入参数：
       labelName ： 标签名称
    输出参数：
        labelName ： 标签名称
    前置接口：
        TestCase新增标签
"""
from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.数据中心.api.标签列表_test import TestCase标签列表 as 标签列表
from yyht.数据中心.api.新增标签_test import TestCase新增标签 as 新增标签
from yyht.数据中心.api.停用标签_test import TestCase停用标签 as 停用标签

class TestCase新增标签(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "names":"${createRandomString(7)}"

        }
    )

    teststeps = [
        Step(
            RunTestCase("新增标签").with_variables(
                **{
                    "labelName": "$names",
                }

            ).call(新增标签).teardown_hook("${sleep_N_secs(3}")
        ),
        Step(
            RunTestCase("搜索标签列表").with_variables(
                **{
                    "name": "$names",
                }

            ).call(标签列表).export(*["name", "disabled", "categoryCode", "id"])
                .teardown_hook("${assert_equal($name,$names)}")
        ),
        Step(
            RunTestCase("启用标签").with_variables(
                **{
                    "disabled": 0,
                    "labelId": "$id",
                    "labelName": "$names",
                    "categoryCode": "$categoryCode",
                }

            ).call(停用标签)
        ),
        Step(
            RunTestCase("搜索标签列表").with_variables(
                **{
                    "name": "$names",
                }

            ).call(标签列表).export(*["name", "disabled", "categoryCode", "id"])
                .teardown_hook("${assert_equal($disabled,0)}")
        ),
        Step(
            RunTestCase("停用标签").with_variables(
                **{
                    "disabled": 1,
                    "labelId": "$id",
                    "labelName": "$names",
                    "categoryCode": "$categoryCode",
                }

            ).call(停用标签)
        ),
        Step(
            RunTestCase("标签列表").with_variables(
                **{
                    "name": "$names",
                }

            ).call(标签列表)
                .teardown_hook("${assert_equal($disabled,1)}")
        ),



    ]

if __name__ == "__main__":
    TestCase新增标签().test_start()

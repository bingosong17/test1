# NOTE: Generated By HttpRunner v3.1.3
"""
    概要：
        bd对公海店铺注册中用户拜访，bdm在拜访管理中验证bd对该店铺拜访的有效性
    输入参数：
        "phone": bd手机号，需要有公海海店铺
        "shopId": bd公海店铺中可进行拜访的店铺id
        "status": 客户状态(0 已停业 1 正常 2 黑名单 3 注册中 4 未审核 5 审核未通过 6 待平台复审)
    输出参数：
        无
    前置接口：
        无
"""

from httprunner import HttpRunner, Config, Step, RunTestCase
from ppApp.业务脚本.私海店铺拜访_test import TestCase私海店铺拜访 as 私海店铺拜访
from ppApp.业务脚本.公海店铺拜访_test import TestCase公海店铺拜访 as 公海店铺拜访
from yyht.权限管理.拼拼账号管理.业务脚本.根据bd寻找bdm_test import TestCase根据bd寻找bdm as 根据bd寻找bdm
from ppApp.业务脚本.bdm查看拜访管理_test import TestCasebdm查看拜访管理 as bdm查看拜访管理
from ppApp.api.查询拜访数据_test import TestCase查询拜访数据 as 查询拜访数据


class TestCase公海店铺注册中用户拜访(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "phone": "15757113586",
            "status": 3,
            "shopId": "${拼拼公私海店铺生成个未拜访的店铺id($phone,1,$status)}",
        })

    teststeps = [
        Step(
            RunTestCase("公海店铺拜访").call(公海店铺拜访)
            .teardown_hook("${sleep_N_secs(1)}")
        ),
        Step(
            RunTestCase("根据bd信息寻找他的bdm信息").with_variables(
                **{
                    "bdPhone": "$phone",
                }
            ).call(根据bd寻找bdm)
            .export(*["bdId", "bdPhone"])
            .teardown_hook("${sleep_N_secs(1)}")
        ),
        Step(
            RunTestCase("bdm查看拜访管理").with_variables(
                **{
                    "phone": "$bdPhone",
                    "operatorId": "$bdId",
                }
            ).call(bdm查看拜访管理)
            .export(*["SignShopPageData"])
            .teardown_hook("${assert_contains($SignShopPageData,shopId=intType$shopId)}")
            .teardown_hook("${sleep_N_secs(15)}")
        ),
        # 目前拜访管理中点击bd拜访记录中，有效拜访未过滤不正常数据，例如黑名单，下版本优化
        # Step(
        #     RunTestCase("查询拜访数据").call(查询拜访数据).export(*["visits"])
        #     .teardown_hook("${assert_pageDataLength($SignShopPageData,$visits)}")
        # ),
    ]


if __name__ == "__main__":
    TestCase公海店铺注册中用户拜访().test_start()

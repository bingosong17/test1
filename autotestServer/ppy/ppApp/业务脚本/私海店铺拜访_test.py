# NOTE: Generated By HttpRunner v3.1.3
"""
    概要：
        从私海列表中添加店铺到拜访计划
    输入参数：
       "phone": 登陆用户手机号码
       "visitTime": 拜访时间
    输出参数：
        无
    前置接口：
        用户登陆；获取私海列表
"""

from httprunner import HttpRunner, Config, Step, RunTestCase
from yyht.用户中心.api.商铺明细_test import TestCase商铺明细 as 商铺明细
from ppApp.api.到店打卡签到保存_test import TestCase到店打卡签到保存 as 到店打卡签到保存
from ppApp.api.更新离店打卡签退_test import TestCase更新离店打卡签退 as 更新离店打卡签退


class TestCase私海店铺拜访(HttpRunner):
    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "ppApp",
            "phone": "15757113586",
            "session": "${getSession($business,$phone)}",
            "shopId": "${拼拼公私海店铺生成个未拜访的店铺id($phone,0)}",
        })

    teststeps = [
        Step(
            RunTestCase("商铺明细").with_variables(
                **{
                    "business": "yyht",
                    "session": "${getSession($business)}",
                    "shopId": "$shopId"
                }
            ).call(商铺明细)
                .export(*["longitude", "latitude"])
                .teardown_hook("${sleep_N_secs(1)}")
        ),
        Step(
            RunTestCase("到店打卡签到保存").call(到店打卡签到保存)
                .export(*["signId"])
                .teardown_hook("${sleep_N_secs(1)}")
        ),
        Step(
            RunTestCase("更新离店打卡签退").with_variables(
                **{
                    "signId": "$signId",
                    "leaveLatitude": "$latitude",
                    "leaveLongitude": "$longitude",
                }
            ).call(更新离店打卡签退)
                .teardown_hook("${sleep_N_secs(1)}")
        ),
    ]


if __name__ == "__main__":
    TestCase私海店铺拜访().test_start()

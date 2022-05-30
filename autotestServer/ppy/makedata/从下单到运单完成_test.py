"""
    概要：
        司机完成取货送货流程
    输入参数：
        "phoneToWl":司机手机号
        "phoneToPpy":拼便宜app登陆手机号
        "goodsId":商品id
        "goodsNu":商品数量
    输出参数：
        无
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from makedata.从下单到生成待接运单_test import TestCase下单运单生效 as 下单运单生效
from makedata.司机完成运单取货送货_test import TestCase司机完成运单 as 司机完成运单


class TestCase下单运单生效(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "phoneToWl": "13738113393",
            "phoneToPpy": "13656669146",
            "goodsId": "10555",
            "goodsNu": 10
        }
    )

    teststeps = [
        Step(
            RunTestCase("下单运单生效").call(下单运单生效).export(*["orderNo"])
            .teardown_hook("${sleep_N_secs(3)}")
        ),
        Step(
            RunTestCase("司机完成运单").call(司机完成运单)
            .teardown_hook("${sleep_N_secs(1)}")
        ),
    ]


if __name__ == "__main__":
    TestCase下单运单生效().test_start()

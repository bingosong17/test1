"""
    概要：
        店铺用户对商品下单，生成订单，最后生成代接运单（运单，订单，商品一一对应）
    输入参数：
        "phone": 运营后台登陆账号,
        "pass": 运营后台登陆密码
        "phoneToPpy": 店铺用户手机号
        "goodsId":商品id
        "goodsNu": 商品数量
        "cityCode": 城市编码
        "phoneToWl": 司机号码
        "drivetime":为订单派车时，设置派单距离目前时间，单位小时
    输出参数：
        orderNo:订单编号
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from makedata.用户下单_test import TestCase用户下单 as 用户下单
from makedata.订单派单生效_test import TestCase订单派单生效 as 订单派单生效
from makedata.订单生成运单_test import TestCase订单生成运单 as 订单生成运单


class TestCase下单运单生效(HttpRunner):

    config = Config("testcase description").verify(False).variables(
        **{
            "phoneToWl": "13738113393",
            "drivetime": "2",
            "phoneToPpy": "15825759189",
            "goodsId": "3965",
            "goodsNu": 5
        }
    ).export(*["orderNo"])

    teststeps = [
        Step(
            RunTestCase("用户下单").call(用户下单).export(*["orderNo"])
            .teardown_hook("${sleep_N_secs(1)}")
        ),
        Step(
            RunTestCase("订单派单生效").call(订单派单生效)
            .teardown_hook("${sleep_N_secs(1)}")
        ),
        Step(
            RunTestCase("订单生成运单").with_variables(
                **{
                    "plannedStartTime": "${hapentime($drivetime)}"
                }
            ).call(订单生成运单)
        ),
    ]


if __name__ == "__main__":
    TestCase下单运单生效().test_start()


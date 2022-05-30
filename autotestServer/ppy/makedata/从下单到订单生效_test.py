"""
    概要：
        店铺用户对商品下单，生成订单，使订单生效
    输入参数：
        "phone": 运营后台登陆账号,
        "pass": 运营后台登陆密码
        "cityCode": 运营后台登陆选择城市
        "phoneToPpy": 店铺用户手机号
        "goodsId":商品id
        "goodsNu": 商品数量
    输出参数：
        orderNo:订单编号
    前置接口：
        无
"""
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from makedata.用户下单_test import TestCase用户下单 as 用户下单
from makedata.订单派单生效_test import TestCase订单派单生效 as 订单派单生效


class TestCase下单订单生效(HttpRunner):

    config = Config("testcase description").verify(False).variables(
        **{
            "phoneToPpy": "15372032298",
            "goodsId": "6565",
            "goodsNu": 10
        }
    ).export(*["orderNo"])

    teststeps = [
        Step(
            RunTestCase("用户下单").call(用户下单).export(*["orderNo"])
                .teardown_hook("${sleep_N_secs(1)}")
        ),
        Step(
            RunTestCase("订单派单生效").call(订单派单生效)
        ),
    ]


if __name__ == "__main__":
    TestCase下单订单生效().test_start()


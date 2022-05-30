"""
    概要：
        店铺用户对商品下单，生成订单（订单中只包括单一商品）
    输入参数：
        "phone": 运营后台登陆账号,
        "pass": 运营后台登陆密码
        "cityCode": 运营后台登陆选择城市
        "phoneToPpy": 店铺用户手机号
        "sessionToPpy": 拼便宜
        "goodsId":商品id
        "goodsNu": 商品数量
    输出参数：
        orderNo:订单编号
    前置接口：
        无
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from yyht.用户中心.业务脚本.商店账户充钱_test import TestCase商店账户充钱 as 商店账户充钱
from ppyApp.业务脚本.用户下单fast_test import TestCase用户下单 as 用户下单


class TestCase用户下单(HttpRunner):

    config = Config("testcase description").verify(False).variables(
        **{
            "phoneToPpy": "13656669146",
            "goodsId": "10555",
            "goodsNu": 10
        }
    ).export(*["orderNo"])

    teststeps = [
        Step(
            RunTestCase("商店账户充钱").with_variables(
                **{
                    "business": "yyht",
                    "tradeAmount": "10000",
                    "userphone": "$phoneToPpy",
                }
            ).call(商店账户充钱)
        ),
        Step(
            RunTestCase("用户下单").with_variables(
                **{
                    "phone": "$phoneToPpy",
                }
            ).call(用户下单).export(*["orderNo"])
        ),
    ]


if __name__ == "__main__":
    TestCase用户下单().test_start()



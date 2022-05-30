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

    前置接口：
        无
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from ppApp.api.获取个人信息_test import TestCase获取个人信息 as 获取bd信息
from yyht.商圈管理.便利店战区管理.业务脚本.获取战区内有效经纬度_test import TestCase获取战区内有效经纬度 as 获取战区内有效经纬度
from ppyApp.业务脚本.新用户注册_test import TestCase新用户注册 as 新用户注册
from ppApp.业务脚本.店铺审核_test import TestCase店铺审核 as 店铺审核

class TestCaseppy用户注册(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "phoneToPpy": "16666666655",
            "phoneToPp": "15757113586",
            "shopName": "${timeStr()}",
        }
    )

    teststeps = [
        Step(
            RunTestCase("获取bd信息").with_variables(
                **{
                    "phone": "$phoneToPp",
                }
            ).call(获取bd信息).export(*["bdId", "bdName", "regionName"])
                .teardown_hook("${sleep_N_secs(1)}")
        ),
        Step(
            RunTestCase("获取战区内有效经纬度").with_variables(
                **{
                    "regionName": "$regionName",
                }
            ).call(获取战区内有效经纬度).teardown_hook("${sleep_N_secs(1)}")
        ),
        Step(
            RunTestCase("新用户注册").with_variables(
                **{
                    "account": "$phoneToPpy",
                    "shareCode": "$bdId",
                    "longitude": "${getLongitude()}",
                    "latitude": "${getLatitude()}",
                    "shopName": "$shopName",
                }
            ).call(新用户注册)
        ),
        Step(
            RunTestCase("店铺审核").with_variables(
                **{
                    "phone": "$phoneToPp",
                    "name": "$shopName"
                }
            ).call(店铺审核)
        ),
    ]


if __name__ == "__main__":
    TestCaseppy用户注册().test_start()

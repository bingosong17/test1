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
from ppyApp.api.获取商品明细_test import TestCase获取商品明细 as 获取商品明细
from ppyApp.api.添加商品_test import TestCase添加商品 as 添加商品
from ppyApp.api.创建订单_test import TestCase创建订单 as 创建订单
from ppyApp.api.发起支付_test import TestCase发起支付 as 发起支付
from ppyApp.api.获取订单详情_test import TestCase获取订单详情 as 获取订单详情
from yyht.用户中心.业务脚本.商店账户充钱_test import TestCase商店账户充钱 as 商店账户充钱
from yyht.订单中心.api.全部订单列表_test import TestCase全部订单列表 as 订单查询
from yyht.物流中心.新派物流.api.新增车辆订单信息_test import TestCase新增车辆订单信息 as 新增车辆信息


class TestCase下单运单生效(HttpRunner):

    config = Config("testcase description").verify(False).variables(
        **{
            "phoneToWl": "13738113393",
            "drivetime": "2",
            "phoneToPpy": "15825759189",
            "goodsId": "3965",
            "goodsNu": 4
        }
    ).export(*["orderNo"])

    teststeps = [
        # 账号 13474088693  货到付款
        Step(
            RunTestCase("添加商品到购物车").with_variables(
                **{
                    "goodsNu": 6,
                    "goodsId": "202414",    # 添加葵花籽
                }
            ).call(添加商品)
        ),
        Step(
            RunTestCase("添加商品到购物车").with_variables(
                **{
                    "goodsNu": 4,
                    "goodsId": "156331",    # 添加可口可乐
                }
            ).call(添加商品)
        ),
        Step(
            RunTestCase("货到付款").with_variables(
                **{
                    "cashOnDelivery": True,
                    "deliverRuleCode": "1"
                }
            ).call(创建订单).export(*["orderNo"])
        ),
        # Step(
        #     RunTestCase("订单查询").with_variables(
        #         **{
        #
        #             "orderNo": "$orderNo"
        #
        #         }
        #     ).call(订单查询).export(*["orderList"]).teardown_hook("${sleep_N_secs(4)}")
        # ),
        # 账号 17629262210  在线支付

        Step(
            RunTestCase("商店账户充钱").with_variables(
                **{
                    "business": "yyht",
                    "tradeAmount": "21000",
                    "userphone": "$phoneToPpy",
                }
            ).call(商店账户充钱)
        ),
        Step(
            RunTestCase("添加商品到购物车").with_variables(
                **{
                    "goodsNu": 6,
                    "goodsId": "202414",  # 添加葵花籽
                }
            ).call(添加商品)
        ),
        Step(
            RunTestCase("添加商品到购物车").with_variables(
                **{
                    "goodsNu": 4,
                    "goodsId": "156331",  # 添加可口可乐
                }
            ).call(添加商品)
        ),
        Step(
            RunTestCase("在线支付").with_variables(
                **{
                    "cashOnDelivery": False,
                    "deliverRuleCode": "1"
                }
            ).call(创建订单).export(*["orderNo"])
        ),
        Step(
            RunTestCase("余额发起支付").with_variables(
                **{

                        "tradeChannel": 10,
                        "useBalance": True

                }
            ).call(发起支付).teardown_hook("${sleep_N_secs(4)}")
        ),
        # Step(
        #     RunTestCase("订单查询").with_variables(
        #         **{
        #
        #             "orderNo": "$orderNo"
        #
        #         }
        #     ).call(订单查询).export(*["orderList"]).teardown_hook("${sleep_N_secs(4)}")
        # ),
        Step(
            RunTestCase("新增车辆信息").with_variables(
                **{

                    "cityCode": "100001",
                    "orderIdList": "2020081016494811212863-2",
                    "vehicleId": 12,
                }
            ).call(新增车辆信息).export(*["tempDistributeId", "virtualTransportationId", "uuid"]).teardown_hook("${sleep_N_secs(4)}")
        ),

    ]


if __name__ == "__main__":
    TestCase下单运单生效().test_start()


# NOTE: Generated By HttpRunner v3.1.3
"""
    概要：
        购物车减少商品
    输入参数：
        "goodsCountToDelete": 商品数量(最小值1)
        "goodsIdToDelete": 商品ID
        "preGoodsToDelete": 是否组合商品(取自商品信息preGoods)
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase减少商品(HttpRunner):

    config = Config("减少商品").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "",
            "token": "",
            "goodsCountToDelete": 6,
            "goodsIdToDelete": "39088",
            "preGoodsToDelete": "false"
        })

    teststeps = [
        Step(
            RunRequest("/ppy-mall/user/cart/v2")
            .delete("/user/cart/v2")
            .with_headers(
                **{
                    "serviceName": "MALL",
                    "channel": "app",
                    "deviceId": "2cdf701146c959d296b4b455f9623536",
                    "version": "4.4.0",
                    "sessionId": "$token",
                    "Content-Length": "51",
                    "Connection": "close",
                    "Accept-Encoding": "gzip",
                    "User-Agent": "okhttp/3.12.0",
                    "Content-Type": "application/json",
                    "Accept-Language": "zh-CN,zh;q=0.8",
                }
            )
            .with_json({
                "goodsCount": "$goodsCountToDelete",
                "goodsId": "$goodsIdToDelete",
                "preGoods": "$preGoodsToDelete"
                })
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase减少商品().test_start()

# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        无
    输入参数：
        无
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase新增会员商品(HttpRunner):

    config = Config("新增会员商品").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "startTime": "2020-09-19 00:00:00",
            "endTime": "2020-10-31 00:00:00",
            "goodsId": 37,
        }).export(*["msg"])

    teststeps = [
        Step(
            RunRequest("/test_t/mall/member/goods")
            .post("/mall/member/goods")
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Content-Length": "386",
                    "sessionId": "$session",
                    "Sec-Fetch-Dest": "empty",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                    "systemCode": "yypp",
                    "Content-Type": "application/json",
                    "Accept": "*/*",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                }
            )
            .with_json(
                {
                    "batchNumber": "",
                    "goodsId":"$goodsId",
                    "redPacketAvailable": 0,
                    "goodsList": [
                        {
                            "memberGoodsId": None,
                            "startTime": "$startTime",
                            "endTime": "$endTime",
                            "sellOn": None,
                            "maxNum": "2",
                            "initStock": "222",
                            "sellPrice": 23,
                            "minSupplierPrice": 0.01,
                            "traId": 11,
                            "traName": "婊ㄦ睙-鍟嗗湀",
                            "levelPrices": None,
                            "_checked": True,
                            "_disabled": False,
                            "memberGoods": [{"memberPrice": "20", "memberLevelId": 4}],
                        }
                    ],
                }
            ).extract()
            .with_jmespath("body.msg", "msg")
            .validate()
            .assert_equal("status_code", 200)
            # .assert_equal("body.statusCode", 2000)
            # .assert_equal("body.body", True)
        ),
    ]


if __name__ == "__main__":
    TestCase新增会员商品().test_start()

'''{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: null",
	"timestamp": 1600419616,
	"signType": null,
	"sign": null,
	"body": true
}'''

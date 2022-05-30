# NOTE: Generated By HttpRunner v3.1.3
"""
    概要：
        订单派单生效
    输入参数：
        "orderNo": 订单编号
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase



class TestCase订单派单生效(HttpRunner):

    config = Config("订单派单生效").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "",
            "session": "",
            "orderNo": "2020082610413214718486",
        })

    teststeps = [
        Step(
            RunRequest("/alpha_t/ppy-op-api/order/takeEffectOrder")
            .post(
                "/ppy-op-api/order/takeEffectOrder"
            )
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Content-Length": "434",
                    "sessionId": "$session",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
                    "systemCode": "yypp",
                    "Content-Type": "application/json",
                    "Accept": "*/*",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7",
                }
            )
            .with_json(
                {
                    "isPay": "",
                    "payType": "",
                    "status": "",
                    "queryType": "",
                    "cloudType": "",
                    "labelCode": "",
                    "orderSource": "",
                    "backGoodsType": "",
                    "settleStatus": "",
                    "spellZoneCode": "",
                    "logisticsStatus": "",
                    "isInsufficient": "",
                    "orderClassify": "",
                    "orderNo": "$orderNo",
                    "pageNum": 1,
                    "pageSize": 10,
                    "sort": True,
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
            .assert_equal("body.body", "订单派单生效成功")
        ),
    ]


if __name__ == "__main__":
    TestCase订单派单生效().test_start()

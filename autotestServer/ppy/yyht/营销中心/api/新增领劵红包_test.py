# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        新增领劵红包
    输入参数：
         "packetName": "领劵红包", 红包名称
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase新增领劵红包(HttpRunner):

    config = Config("新增领劵红包").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "packetName": "领劵红包",
        })

    teststeps = [
        Step(
            RunRequest("/test_t/mall/redPacket")
            .post("/mall/redPacket")
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Content-Length": "246",
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
                    "packetName": "$packetName",
                    "instructions": "领劵红包",
                    "receiveType": "11",
                    "packetType": "02",
                    "availableOrderAmount": 0,
                    "packetAmount": 1.1,
                    "timeType": 1,
                    "availableGoodsType": 1,
                    "goodsAttributes": [],
                    "dayOffset": "100",
                    "accountPush": 0,
                    "expirePush": 0,
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
            .assert_equal("body.body", True)
        ),
    ]


if __name__ == "__main__":
    TestCase新增领劵红包().test_start()

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


class TestCase新增返利商品(HttpRunner):

    config = Config("新增返利商品").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "",
            "session": "",
            "startTime": "${hapentime(1)}"+":00",
            "endTime": "${hapentime(100)}"+":00",
            "rebateAmount": 1,
            "goodsId": "5645",
        })

    teststeps = [
        Step(
            RunRequest("/test_t/mall/rebate/add")
            .post("/mall/rebate/add")
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Content-Length": "101",
                    "sessionId": "$session",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
                    "systemCode": "yypp",
                    "Content-Type": "application/json",
                    "Accept": "*/*",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                }
            )
            .with_json(
                {
                    "startTime": "$startTime",
                    "endTime": "$endTime",
                    "rebateAmount": "$rebateAmount",
                    "goodsId": "$goodsId",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
            .assert_equal("body.body", True)
        ),
    ]


if __name__ == "__main__":
    TestCase新增返利商品().test_start()

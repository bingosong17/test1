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


class TestCase删除爆品(HttpRunner):

    config = Config("删除爆品").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "",
            "session": "",
            "surpriseId": "3220171"
        })

    teststeps = [
        Step(
            RunRequest("/test_t/mall/promo/delete")
            .get("/mall/promo/delete")
            .with_params(**{"surpriseId": "$surpriseId"})
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "sessionId": "$session",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                    "systemCode": "yypp",
                    "Accept": "*/*",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
            .assert_equal("body.body", True)
        ),
    ]


if __name__ == "__main__":
    TestCase删除爆品().test_start()

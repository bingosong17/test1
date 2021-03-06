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

import env
class TestCase推荐置顶(HttpRunner):

    config = Config("推荐置顶").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
        })

    teststeps = [
        Step(
            RunRequest("/mall/sell/recommend")
            .post("/mall/sell/recommend")
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Content-Length": "28",
                    "Accept": "application/json, text/plain, */*",
                    "Sec-Fetch-Dest": "empty",
                    "key": "",
                    "sessionId": "$session",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Sec-Fetch-Site": "same-site",
                    "Sec-Fetch-Mode": "cors",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                }
            )
            .with_data({"id": "1529", "traId": "11", "sortIndex": "1"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
            .assert_equal("body.msg", "推荐成功")
            .assert_equal("body.body", True)
        ),
    ]


if __name__ == "__main__":
    TestCase推荐置顶().test_start()

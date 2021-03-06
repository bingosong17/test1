# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        无
    输入参数：
        "traId": 商圈ID
        "sortId": 排序ID
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase取消推荐(HttpRunner):

    config = Config("取消推荐").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "traId": "11",
            "sortId": "3452"
        })

    teststeps = [
        Step(
            RunRequest("/mall/sell/cancelRecommend")
            .get("/mall/sell/cancelRecommend")
            .with_params(**{"traId": "$traId", "sortId": "$sortId"})
            .with_headers(
                **{
                    "Connection": "keep-alive",
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
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase取消推荐().test_start()

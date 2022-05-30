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


class TestCase删除广告(HttpRunner):

    config = Config("删除广告").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
        }).export(*["msg"])

    teststeps = [
        Step(
            RunRequest("/mall/shopping/launch/$launchId/drop")
            .post("/mall/shopping/launch/$launchId/drop")
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Content-Length": "0",
                    "Accept": "application/json, text/plain, */*",
                    "Sec-Fetch-Dest": "empty",
                    "sessionId": "$session",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                    "Sec-Fetch-Site": "same-site",
                    "Sec-Fetch-Mode": "cors",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
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
    TestCase删除广告().test_start()

# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        修改后台类目
    输入参数：
        "name": 后台类目名称
        "percent": 百分比
        "hotSaleRatio": 热卖比例
        "id": 后台类目编号
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase修改后台类目(HttpRunner):

    config = Config("修改后台类目").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "name": "后台类目0434",
            "percent": 1,
            "hotSaleRatio": 0.01,
            "id": 5306
        })

    teststeps = [
        Step(
            RunRequest("/test_t/ppy-op-api/backstageCategory/modify")
            .post(
                "/ppy-op-api/backstageCategory/modify"
            )
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Content-Length": "69",
                    "sessionId": "$session",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36",
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
                {"name": "$name", "percent": "$percent", "hotSaleRatio": "$hotSaleRatio", "id": "$id"}
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase修改后台类目().test_start()

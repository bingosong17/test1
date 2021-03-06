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


class TestCase停用标签(HttpRunner):

    config = Config("停用标签").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "disabled": 0,
            "labelId": 65,
            "labelName": "test",
            "categoryCode": "005",
        })

    teststeps = [
        Step(
            RunRequest("/test_t/ppy-op-api/label/editLabel")
            .post("/ppy-op-api/label/editLabel")
            .with_headers(
                **{
                    "Content-Length": "68",
                    "sessionId": "$session",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
                    "systemCode": "yypp",
                    "Content-Type": "application/json",
                    "Accept": "*/*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                }
            )
            .with_json(
                {
                    "categoryCode": "$categoryCode",
                    "disabled": "$disabled",
                    "labelId": "$labelId",
                    "labelName": "$labelName",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
            .assert_equal("body.body", "标签编辑成功")
        ),
    ]


if __name__ == "__main__":
    TestCase停用标签().test_start()

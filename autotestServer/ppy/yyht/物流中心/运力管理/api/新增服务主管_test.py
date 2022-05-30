# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        新增服务主管
    输入参数：
        phone   手机号
        name    服务主管名称
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase新增服务主管(HttpRunner):

    config = Config("新增服务主管").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "phone":  "120${createRandomNumber(8)}",
            "name": ""
        })

    teststeps = [
        Step(
            RunRequest("/logis/api/mng/supervisor/create")
            .post("/logis/api/mng/supervisor/create")
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "sessionId": "$session",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Content-Length": "27",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Connection": "keep-alive",
                }
            )
            .with_data({"name": "$name", "phone": "$phone"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
            .assert_equal("body.body", "操作成功")
        ),
    ]


if __name__ == "__main__":
    TestCase新增服务主管().test_start()

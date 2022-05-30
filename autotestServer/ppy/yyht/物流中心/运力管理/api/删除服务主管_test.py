# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        删除服务主管
    输入参数：
        id  服务主管id
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase删除服务主管(HttpRunner):

    config = Config("删除服务主管").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "id": ""
        })

    teststeps = [
        Step(
            RunRequest("/logis/api/mng/supervisor/delete")
            .delete("/logis/api/mng/supervisor/delete")
            .with_params(**{"id": "$id"})
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Accept": "application/json, text/plain, */*",
                    "sessionId": "$session",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
            .assert_equal("body.body", "操作成功")
        ),
    ]


if __name__ == "__main__":
    TestCase删除服务主管().test_start()

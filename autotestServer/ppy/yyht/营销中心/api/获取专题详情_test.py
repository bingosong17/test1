# NOTE: Generated By HttpRunner v3.1.3
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


class TestCase获取专题详情(HttpRunner):

    config = Config("获取专题详情").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "topicId":"12164"
        })

    teststeps = [
        Step(
            RunRequest("/alpha_t/mall/shopping/topics/12164/goods")
            .get(
                "/mall/shopping/topics/$topicId/goods"
            )
            .with_params(
                **{
                    "pageNum": "1",
                    "pageSize": "10",
                    "queryType": "",
                    "queryValue": "",
                    "sellOn": "",
                    "labelCode": "",
                    "backstageCategoryId": "",
                }
            )
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "sessionId": "$session",
                    "Sec-Fetch-Dest": "empty",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                    "systemCode": "yypp",
                    "Accept": "*/*",
                    "Sec-Fetch-Site": "same-origin",
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
    TestCase获取专题详情().test_start()

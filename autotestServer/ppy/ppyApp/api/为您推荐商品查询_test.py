# NOTE: Generated By HttpRunner v3.1.3
"""
    概要：
        为您推荐商品查询
    输入参数：

    输出参数：

    前置接口：
        验证码登陆
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase为您推荐商品查询(HttpRunner):

    config = Config("为您推荐商品查询").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "",
            "token": "",
        })

    teststeps = [
        Step(
            RunRequest("/ppy-mall/search/goods/recommend")
            .get("/search/goods/recommend")
            .with_params(**{"pageNum": "1", "pageSize": "10"})
            .with_headers(
                **{
                    "serviceName": "MALL",
                    "channel": "app",
                    "deviceId": "2cdf701146c959d296b4b455f9623536",
                    "version": "4.4.0",
                    "sessionId": "$token",
                    "Connection": "close",
                    "Accept-Encoding": "gzip",
                    "User-Agent": "okhttp/3.12.0",
                    "Content-Type": "application/json",
                    "Accept-Language": "zh-CN,zh;q=0.8",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase为您推荐商品查询().test_start()

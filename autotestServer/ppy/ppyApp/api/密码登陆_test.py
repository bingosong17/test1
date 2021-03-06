# NOTE: Generated By HttpRunner v3.1.3
"""
    概要：
        用户对指定商品下单，使用账户余额付款
    输入参数：
        "phone": 登陆账号,
        "pass": 登陆密码,
    输出参数：
        'token':登陆凭证
    前置接口：
        无
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase密码登陆(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "",
            "phone": "13362140179",
            "pass": "140179",
    }).export(*['token'])

    teststeps = [
        Step(
            RunRequest("/ppy-mall/user/account/login")
            .get("/user/account/login")
            .with_params(**{"account": "$phone", "password": "$pass"})
            .with_headers(
                **{
                    "serviceName": "MALL",
                    "channel": "app",
                    "deviceId": "2cdf701146c959d296b4b455f9623536",
                    "version": "4.4.0",
                    "sessionId": "",
                    "Connection": "close",
                    "Accept-Encoding": "gzip",
                    "User-Agent": "okhttp/3.12.0",
                    "Content-Type": "application/json",
                    "Accept-Language": "zh-CN,zh;q=0.8",
                }
            ).extract()
            .with_jmespath("body.body.token", "token")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
            ),
    ]


if __name__ == "__main__":
    TestCase密码登陆().test_start()

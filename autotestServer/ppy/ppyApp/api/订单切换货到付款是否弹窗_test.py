# NOTE: Generated By HttpRunner v3.1.3
"""
    概要：
        订单切换货到付款是否弹窗
    输入参数：

    输出参数：

    前置接口：
        验证码登陆
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase订单切换货到付款是否弹窗(HttpRunner):

    config = Config("订单切换货到付款是否弹窗").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "",
            "token": "",

            "orderNo":""
        })

    teststeps = [
        Step(
            RunRequest("/ppy-mall/orders/2020081216352711217645/switchOnDeliveryValid")
            .get(
                "/orders/$orderNo/switchOnDeliveryValid"
            )
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
            .assert_equal("body.body", False)
        ),
    ]


if __name__ == "__main__":
    TestCase订单切换货到付款是否弹窗().test_start()

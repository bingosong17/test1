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


class TestCase生成组合图片(HttpRunner):

    config = Config("生成组合图片").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "goodsId": "495",
            "goodsId2": "550",
        }).export(*["body"])

    teststeps = [
        Step(
            RunRequest("/beta_t/mall/shopping/combo/meal/generateComboImage")
            .get(
                "/mall/shopping/combo/meal/generateComboImage"
            )
            .with_params(**{"goodsIds": "$goodsId,$goodsId2"})
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
            ).extract()
            .with_jmespath("body.body[0]", 'body')
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase生成组合图片().test_start()
body = '''{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: null",
	"timestamp": 1600242530,
	"signType": null,
	"sign": null,
	"body": ["http://images.alpha.pinpianyi.cn/images/common/8b6eeb989e1a45a3bbd7aa1b6f236596.png"]
}'''